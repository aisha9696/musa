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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexProductsListView.as_view(), name='index'),
    path('product/<int:id>', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:product_id>/update', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:product_id>/delete', views.ProductDeleteView.as_view(), name='product_delete'),
    path('product/add', views.ProductCreateView.as_view(), name='product_add'),
    path('product/<int:product_id>/reviews', views.ReviewCreateView.as_view(), name='review_add'),
    path('review/<int:id>', views.ReviewDetailView.as_view(), name='review_detail'),
    path('review/<int:review_id>/update', views.ReviewUpdateView.as_view(), name='review_update'),
    path('review/<int:review_id>/delete', views.ReviewDeleteView.as_view(), name='review_delete'),
    path('accounts/', include('accounts.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
