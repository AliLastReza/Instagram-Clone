from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import generics
from user.api.serializers import UserSerializer
from rest_framework import viewsets

User = get_user_model()


class ProfileRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = 'username'
    lookup_field = 'username'

class ProView(viewsets.ModelViewSet):
    pass

class ProfileRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user