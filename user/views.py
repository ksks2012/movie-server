from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from user.serializers import UserSerializer


class UserViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated()]

    def get_permissions(self):
        if self.action in ('create', 'login'):
            return [AllowAny()]
        return self.permission_classes

    def create(self, request):
        """
        - 회원 가입
        - POST users/
        """
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create(**serializer.validated_data)
        token = Token.objects.create(user=user)
        return Response(UserSerializer(user).data)

    @action(detail=False, methods=['POST'])
    def login(self, request):
        """
        - 로그인
        - POST users/login/
        """
        user = authenticate(request, username=request.data.get('username'), password=request.data.get('password'))
        if user is None:
            return Response(dict(error="Wrong username or wrong password"), status=status.HTTP_400_BAD_REQUEST)
        login(request, user)
        data = UserSerializer(user).data
        return Response(data)

    @action(detail=False, methods=['POST'])
    def logout(self, request):
        """
        - 로그아웃
        - POST users/logout/
        """
        logout(request)
        return Response()
