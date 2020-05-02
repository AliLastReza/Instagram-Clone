from django.urls import path

from relation.views import FollowView, FollowerListView, FollowingListView, \
    FollowerListAPIView

urlpatterns = [
    path('<str:username>/follow/', FollowView.as_view(), name='follow-unfollow'),
    path('<str:username>/followers/', FollowerListView.as_view(), name="followers"),
    path('<str:username>/followings', FollowingListView.as_view(), name="followings"),
    path('followers/', FollowerListAPIView.as_view(), name='followers_api')
]
