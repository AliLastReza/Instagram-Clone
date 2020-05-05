from django.urls import path

from relation.views import FollowersListAPIView

urlpatterns = [
    path('followers/', FollowersListAPIView.as_view(), name='followers'),
]
