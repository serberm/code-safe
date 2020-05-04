from django.urls import path
from . import views

urlpatterns = [
  path('login', views.login),
  path('signup', views.signup),
  path('signup_processing', views.signup_processing),
  path('login_processing', views.login_processing),
  path('dashboard', views.dashboard),
]