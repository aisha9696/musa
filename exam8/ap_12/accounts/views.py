from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView

from accounts import forms, models

from django.views import generic
from django.contrib.auth import login, get_user_model, mixins, views
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator


class RegisterView(generic.CreateView):
    model = get_user_model()
    template_name = 'auth/register.html'
    form_class = forms.RegisterForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect(self.get_success_url())

    def get_success_url(self):
        return self.request.POST.get(
            'next',
            self.request.GET.get('next', '')
        )


class UserDetailView(generic.DetailView):
    model = get_user_model()
    template_name = 'auth/user_detail.html'
    context_object_name = 'user_obj'
    pk_url_kwarg = 'id'
    paginate_by = 3
    paginate_orphans = 0

    def __get_paginator(self):
        reviews = self.object.reviews.all()
        return Paginator(reviews, self.paginate_by, self.paginate_orphans)

    def get_context_data(self, **kwargs):
        user = get_object_or_404(self.model, pk=self.kwargs.get('id'))
        models.Profile.objects.get_or_create(user=user)

        paginator = self.__get_paginator()

        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)

        return super().get_context_data(
            **kwargs,
            paginator=paginator,
            page_obj=page,
            is_paginated=page.has_other_pages(),
        )


class UserUpdateView(UserPassesTestMixin, generic.UpdateView):
    model = get_user_model()
    form_class = forms.UserUpdateForm
    template_name = 'auth/user_update.html'
    context_object_name = 'user_obj'
    pk_url_kwarg = 'id'

    def test_func(self):
        return self.request.user == self.get_object()

    def get_context_data(self, **kwargs):

        if 'profile_form' not in kwargs:
            kwargs['profile_form'] = self.get_profile_form()

        return super().get_context_data(**kwargs)

    def get_profile_form(self):
        kwargs = {'instance': self.object.profile}

        if self.request.method == 'POST':
            kwargs['data'] = self.request.POST
            kwargs['files'] = self.request.FILES

        return forms.ProfileUpdateForm(**kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        user_form = self.get_form()
        profile_form = self.get_profile_form()

        if user_form.is_valid() and profile_form.is_valid():
            return self.form_valid(user_form, profile_form)

        return self.form_invalid(user_form, profile_form)

    def form_valid(self, user_form, profile_form):
        response = super().form_valid(user_form)
        profile_form.save()
        return response

    def form_invalid(self, user_form, profile_form):
        context = self.get_context_data(form=user_form, profile_form=profile_form)
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('profile', kwargs={'id': self.object.id})

    def get_object(self, queryset=None):
        return self.request.user


class ChangePasswordView(views.PasswordChangeView):
    form_class = forms.ChangePasswordForm
    template_name = 'auth/change_password.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'id': self.request.user.id})
