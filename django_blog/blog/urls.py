# blog/urls.py
from django.urls import path
from .views import register, user_login, user_logout, profile
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, comment_edit, comment_delete
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    search_posts
)
# blog/urls.py

from .views import posts_by_tag  
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostByTagListView,  # Import the new view
)






urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='tagged-posts'),  # Tagged posts URL
    path('search/', search_posts, name='search-posts'),  # Search URL
    path('', PostListView.as_view(), name='post-list'),  # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View a single post
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Update an existing post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),  # Create a new comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),  # Update a comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),  # Delete a comment
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),  # Create a new comment
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),  # Edit a comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),  # Delete a comment
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
]