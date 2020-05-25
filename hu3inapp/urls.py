from django.urls import path
from .views import (
    PostListView,
    UserPostListView,
    PostDetailView,
    PostDeleteView,
    PostCreateView,
    PostUpdateView,
    FollowListView,
    FollowersListView,
)

app_name = "hu3inapp"
urlpatterns = [
    path('', PostListView.as_view(), name="home"),
    path('post/new/', PostCreateView.as_view(), name="create"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="detail"),
    path('user/<str:username>/', UserPostListView.as_view(), name="user-posts"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="delete"),
    path('user/<str:username>/follows/',
         FollowListView.as_view(), name="follows"),
    path('user/<str:username>/followers',
         FollowersListView.as_view(), name="followers")
]
