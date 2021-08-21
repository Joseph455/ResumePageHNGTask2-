from django.urls import path
from resumeApp import views


urlpatterns = [
    path('', views.home, name="index"),
    path('contact/', views.contact, name="contact"),
]
