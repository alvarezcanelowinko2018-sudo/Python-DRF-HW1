from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from apps.users.serializers import UserSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class BaseUserActionView(GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    def get_object(self):
        user = super().get_object()
        if user == self.request.user:
            raise ValidationError({'detail': 'You cannot change your own status.'})
        if user.is_superuser:
            raise PermissionDenied({'detail': 'You cannot change superuser status.'})
        return user


class UserToAdminView(BaseUserActionView):
    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save(update_fields=['is_staff'])
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserToUserView(BaseUserActionView):
    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            user.is_staff = False
            user.save(update_fields=['is_staff'])
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserBlockView(BaseUserActionView):
    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = False
            user.save(update_fields=['is_active'])
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserUnBlockView(BaseUserActionView):
    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_active = True
            user.save(update_fields=['is_active'])
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)