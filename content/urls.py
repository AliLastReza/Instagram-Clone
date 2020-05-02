from django.urls import path

from content.views import ContentView
from relation.views import FollowView, FollowerListView, FollowingListView, \
    FollowerListAPIView

urlpatterns = [
    path('posts/', ContentView.as_view())
]
