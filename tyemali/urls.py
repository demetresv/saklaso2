from django.contrib import admin
from django.urls import path
from .models import Post,Category
from .views import post_list_and_create


urlpatterns = [
    path('post/', post_list_and_create)
]
