from django.urls import path
from accounts import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from accounts import views
from accounts.views import RegisterView


urlpatterns = [
    path('login', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('<int:id>/', views.UserDetailView.as_view(), name='profile'),
    path('change_password', views.ChangePasswordView.as_view(), name='change_password'),
    path('update', views.UserUpdateView.as_view(), name='user_update'),
]
