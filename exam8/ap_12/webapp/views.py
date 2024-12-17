from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Avg
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView

from webapp.models import Product, Review
from webapp.forms import ProductForm, ReviewForm


class IndexProductsListView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'product'
    model = Product


class ProductDetailView(generic.DetailView):
    pk_url_kwarg = 'id'
    model = Product
    template_name = 'product/detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        reviews = self.object.reviews.order_by('author')
        reviews2 = self.object.reviews.all()
        average_grade = reviews2.aggregate(Avg('grade'))['grade__avg']
        return super().get_context_data(
            **kwargs,
            reviews=reviews,
            review_form=ReviewForm,
            average_grade=average_grade
        )


class ProductUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = Product
    template_name = 'product/update.html'
    form_class = ProductForm
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'
    permission_required = 'webapp.change_product'

    def has_permission(self) -> bool:
        return super().has_permission()

    def get_success_url(self):
        return reverse('product_detail', kwargs={'id': self.object.id})


class ProductDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Product
    pk_url_kwarg = 'product_id'
    permission_required = 'webapp.delete_product'

    def has_permission(self) -> bool:
        return super().has_permission()

    def get_success_url(self):
        return reverse('index')


class ProductCreateView(PermissionRequiredMixin, generic.CreateView):
    model = Product
    template_name = 'product/product.html'
    form_class = ProductForm
    permission_required = 'webapp.add_product'

    def has_permission(self) -> bool:
        return super().has_permission()

    def get_success_url(self):
        return reverse('product_detail', kwargs={'id': self.object.id})


class ReviewCreateView(LoginRequiredMixin, generic.CreateView):
    model = Review
    template_name = 'review/review.html'
    form_class = ReviewForm

    def form_valid(self, form):
        product_id = self.kwargs.get('product_id')
        product = Product.objects.get(id=product_id)
        print(self.kwargs)
        print(form.cleaned_data)
        review = form.save(commit=False)
        review.product = product
        review.author = self.request.user
        review.save()

        return redirect('product_detail', id=product_id)


class ReviewUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = Review
    template_name = 'review/update.html'
    form_class = ReviewForm
    context_object_name = 'review'
    pk_url_kwarg = 'review_id'
    permission_required = 'webapp.change_product'

    def has_permission(self) -> bool:
        return super().has_permission() or self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('product_detail', kwargs={'id': self.object.product.id})


class ReviewDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Review
    pk_url_kwarg = 'review_id'
    permission_required = 'webapp.delete_product'

    def has_permission(self) -> bool:
        return super().has_permission() or self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('product_detail', kwargs={'id': self.object.product.id})


class ReviewDetailView(TemplateView):
    template_name = 'review/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            review = Review.objects.get(id=self.kwargs['id'])
        except Review.DoesNotExist:
            raise Http404("Задача не найдена")
        context['review'] = review
        return context
