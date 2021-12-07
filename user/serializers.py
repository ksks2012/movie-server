from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'token',
        )

    def validate_password(self, value):
        return make_password(value)

    def get_token(self, user):
        token = user.auth_token.key
        return token
