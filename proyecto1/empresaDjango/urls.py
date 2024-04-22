from django.urls import path

from empresaDjango import views

urlpatterns = [
    path('', views.index, name='index'),
]