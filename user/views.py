from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from user.serializers import UserSerializer
from user.services import UserService


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
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

        user = UserService().create(**serializer.validated_data)
        rtn = UserSerializer(user).data
        return Response(rtn, status=status.HTTP_201_CREATED)

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

        rtn = UserSerializer(user).data
        return Response(rtn, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def logout(self, request):
        """
        - 로그아웃
        - POST users/logout/
        """
        logout(request)
        return Response(status=status.HTTP_200_OK)
