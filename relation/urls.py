from django.urls import path

from relation.views import FollowView, FollowerShow, FollowingShow

urlpatterns = [
    path('<str:username>/follow/', FollowView.as_view(), name='follow_unfollow'),
    path('<str:username>/followers/', FollowerShow.as_view(), name='follower-show'),
    path('<str:username>/following/', FollowingShow.as_view(), name='following-show')
    ]
