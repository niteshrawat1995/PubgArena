from django.urls import path

from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView,
                    about)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', about, name='blog-about'),
    path('post/add/', PostCreateView.as_view(), name='blog-add'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='blog-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='blog-delete'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-post'),

]
