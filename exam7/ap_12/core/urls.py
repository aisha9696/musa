"""ap_12 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexListView.as_view(), name='index'),
    path('book/<int:id>', views.BookDetailView.as_view(), name='book_detail'),
    path('book/add', views.BookCreateView.as_view(), name='book_add'),
    path('book/add_by_author/<int:author_id>', views.BookCreateView2.as_view(), name='book_add2'),
    path('book/<int:id>/update', views.BookUpdateView.as_view(), name='book_update'),
    path('book/<int:id>/delete', views.BookDeleteView.as_view(), name='book_delete'),
    path('authors', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:id>', views.AuthorDetailView.as_view(), name='author_detail'),
    path('genres', views.GenreListView.as_view(), name='genres'),
    path('genre/add', views.GenreCreateView.as_view(), name='genre_add'),
    path('genres/<int:genre_id>/delete', views.GenreDeleteView.as_view(), name='genre_delete'),
    path('genre/<int:id>', views.GenreDetailView.as_view(), name='genre_detail'),

]
