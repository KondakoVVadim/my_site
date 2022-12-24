from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('posts/', views.main_blog),
    path('posts/<int:name_post>/',views.name_post),
    path('posts/<str:name_post>/',views.name_post)
]