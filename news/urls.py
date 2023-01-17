from django.urls import path
from django.contrib.auth import views as auth_views
from news import views

urlpatterns = [
    path('', views.home, name="home"),
    path('next', views.loadcontent, name="Loadcontent"),
]