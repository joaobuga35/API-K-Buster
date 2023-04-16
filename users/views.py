from rest_framework.views import APIView, Request, Response, status
from users.serializers import UserSerializer
from users.models import User
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import *

# Create your views here.


class UserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        ...


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [UsersPermission]

    def get(self, request: Request, user_id) -> Response:
        user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request: Request, user_id) -> Response:
        user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(request, user)

        serializer = UserSerializer(user, request.data, partial=True)

        serializer.is_valid()
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    ...
