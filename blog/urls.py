from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('pythonprojects/', views.pythonprojects, name='pythonprojects'),
    path('webdevprojects/', views.webdev, name='webdev'),
    path('mlprojects/', views.mlprojects, name='mlprojects'),
    path('pythonprojects/<str:slug>', views.pythonposts, name='pythonposts'),
    path('webdevprojects/<str:slug>', views.webdevposts, name='webdevposts'),
    path('mlprojects/<str:slug>', views.mlprojectsposts, name='mlprojectspostss'),
]