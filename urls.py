from django.urls import path
from rest_framework import routers
from todoapi import views

urlpatterns = [
  path('todo/', views.TodoApiView.as_view()),
  path('todo/<int:id>/', views.TodoApiView.as_view()),
]