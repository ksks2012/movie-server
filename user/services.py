from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token


class UserService:
    def create(self, **validated_data):
        user = User.objects.create(**validated_data)
        token = Token.objects.create(user=user)
        return user
