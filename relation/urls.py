from django.urls import path

from relation.views import FollowView, FollowerListView, FollowingListView

urlpatterns = [
    path('<str:username>/follow/', FollowView.as_view(), name='follow-unfollow'),
    path('<str:username>/followers/', FollowerListView.as_view(), name="followers"),
    path('<str:username>/followings', FollowingListView.as_view(), name="followings")
]
