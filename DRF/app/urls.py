from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('author/', views.api_author_view, name='authors-list'),
]