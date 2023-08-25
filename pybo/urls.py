from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('my/', views.my)
]
