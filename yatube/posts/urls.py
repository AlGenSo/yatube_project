from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('posts/groups/<slug:slug>',
     views.groups_posts
    ),
]