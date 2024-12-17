from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from webapp.models import Book, Author, Genre
from django.db.models import Q
from webapp.forms import SearchForm, BookForm, GenreForm
from urllib.parse import urlencode
from django.urls import reverse


class IndexListView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'book'
    model = Book
    ordering = ['name']
    paginate_by = 2
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = SearchForm(self.request.GET)
        self.search_value = None

        if self.form.is_valid():
            self.search_value = self.form.cleaned_data['search']

        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['form'] = self.form

        if self.search_value:
            context['query_params'] = urlencode({'search': self.search_value})

        return context

    def get_queryset(self):
        qs = super().get_queryset()

        if self.search_value:
            query = (
                    Q(name__icontains=self.search_value)
                    | Q(author__name__icontains=self.search_value)
                    | Q(genre__name__icontains=self.search_value)
            )
            qs = qs.filter(query).distinct()

        return qs


class BookDetailView(generic.DetailView):
    pk_url_kwarg = 'id'
    model = Book
    template_name = 'book/detail.html'
    context_object_name = 'book'


class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'book/book.html'
    form_class = BookForm

    def get_success_url(self):
        return reverse('book_detail', kwargs={'id': self.object.id})


class BookCreateView2(generic.CreateView):
    model = Book
    template_name = 'book/book.html'
    form_class = BookForm

    def get_initial(self):
        initial = super().get_initial()
        initial['author'] = get_object_or_404(Author, pk=self.kwargs['author_id'])
        return initial

    def get_success_url(self):
        return reverse('book_detail', kwargs={'id': self.object.id})


class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'book/update.html'
    form_class = BookForm
    context_object_name = 'book'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('book_detail', kwargs={'id': self.object.id})


class BookDeleteView(View):
    def post(self, request, *args, **kwargs):
        get_object_or_404(Book, id=kwargs['id']).delete()

        return redirect('index')


class AuthorListView(generic.ListView):
    template_name = 'author/index.html'
    context_object_name = 'author'
    model = Author
    ordering = ['name']
    paginate_by = 2
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = SearchForm(self.request.GET)
        self.search_value = None

        if self.form.is_valid():
            self.search_value = self.form.cleaned_data['search']

        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['form'] = self.form

        if self.search_value:
            context['query_params'] = urlencode({'search': self.search_value})

        return context

    def get_queryset(self):
        qs = super().get_queryset()

        if self.search_value:
            query = (
                    Q(name__icontains=self.search_value)
            )
            qs = qs.filter(query).distinct()

        return qs


class AuthorDetailView(generic.DetailView):
    pk_url_kwarg = 'id'
    model = Author
    template_name = 'author/detail.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        books = self.object.book.order_by('year_of_publishing')
        return super().get_context_data(
            **kwargs,
            books=books,
        )


class GenreListView(generic.ListView):
    template_name = 'genre/genre.html'
    context_object_name = 'genre'
    model = Genre
    ordering = ['name']
    paginate_by = 2
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = SearchForm(self.request.GET)
        self.search_value = None

        if self.form.is_valid():
            self.search_value = self.form.cleaned_data['search']

        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['form'] = self.form

        if self.search_value:
            context['query_params'] = urlencode({'search': self.search_value})

        return context

    def get_queryset(self):
        qs = super().get_queryset()

        if self.search_value:
            query = (
                    Q(name__icontains=self.search_value)
            )
            qs = qs.filter(query).distinct()

        return qs


class GenreCreateView(generic.CreateView):
    model = Genre
    template_name = 'book/book.html'
    form_class = GenreForm

    def get_success_url(self):
        return reverse('genres')


class GenreDeleteView(generic.DeleteView):
    model = Genre
    pk_url_kwarg = 'genre_id'

    def get_success_url(self):
        return reverse('genres')


class GenreDetailView(generic.DetailView):
    pk_url_kwarg = 'id'
    model = Genre
    template_name = 'genre/detail.html'
    context_object_name = 'genre'

    def get_context_data(self, **kwargs):
        books = self.object.book.order_by('year_of_publishing')
        return super().get_context_data(
            **kwargs,
            books=books,
            # tasks_form=ToDoForm,
        )