from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny

from .serializers import ReadOnlyUserSerializer, WriteOnlyUserSerializer, AuthToken
from rest_framework import status
from rest_framework.response import Response

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ReadOnlyUserSerializer
    permission_classes = [ReadOnlyUserSerializer]

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = WriteOnlyUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        password = serializer.data['password']
        username = serializer.data['username']
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        serializer = ReadOnlyUserSerializer(user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = AuthToken