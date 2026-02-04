from rest_framework import serializers
from RegAuth.models import CustomAbstractUser

class CustomAbstractUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomAbstractUser
        fields = ["username", "email", "password"]