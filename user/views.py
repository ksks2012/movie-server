from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated


class UserViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ('create', 'login'):
            return [AllowAny]
        return self.permission_classes

    def create(self, request):
        """
        - 회원 가입
        - POST users/
        """
        pass

    @action(detail=False, methods=['POST'])
    def login(self, request):
        """
        - 로그인
        - POST users/login/
        """
        pass

    @action(detail=False, methods=['POST'])
    def logout(self, request):
        """
        - 로그아웃
        - POST users/logout/
        """
        pass
