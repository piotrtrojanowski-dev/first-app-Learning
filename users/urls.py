"""Definition patters address from users app."""

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]