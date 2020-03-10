from django.urls import path

from user.views import RegisterView, LoginView, ProfileUpdateView, ProfileDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth-register'),
    path('login/', LoginView.as_view(), name='auth-login'),
    path('profile/', ProfileUpdateView.as_view(), name='auth-profile'),
]
