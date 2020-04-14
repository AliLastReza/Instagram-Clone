from django.urls import path

from user.api.views import ProfileRetrieveAPIView

urlpatterns = [
    path('profile/<str:username>/', ProfileRetrieveAPIView.as_view())
]