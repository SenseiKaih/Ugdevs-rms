from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='my_view'),
    path('about/', views.about_view, name='about_view'),
]
