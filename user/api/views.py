from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.api.serializers import UserSerializer

User = get_user_model()


class ProfileRetrieveAPIView(APIView):

    def get(self, request, username, *args, **kwargs):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                {'error': "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = UserSerializer(instance=user)
        return Response(serializer.data)
