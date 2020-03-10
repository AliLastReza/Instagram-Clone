from django.urls import path

from relation.views import FollowView

urlpatterns = [
    path('<str:username>/follow/', FollowView.as_view(), name='follow-unfollow')
]
