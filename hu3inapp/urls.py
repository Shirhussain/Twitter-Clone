from django.urls import path
from . views import PostListView, UserPostListView, PostDetailView

app_name = "hu3inapp"
urlpatterns = [
    path('', PostListView.as_view(), name="home"),
    path('posts/', UserPostListView.as_view(), name="posts"),
    path('detail/<int:pk>/', PostDetailView.as_view(), name="detail"),
]
