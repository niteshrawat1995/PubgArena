from django.contrib import admin
from django.urls import path, include

from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    about)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', about, name='blog-about'),

]