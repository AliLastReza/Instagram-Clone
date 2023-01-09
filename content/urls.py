from django.urls import path

from content.views import PostListCreateAPIView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='posts'),
]
