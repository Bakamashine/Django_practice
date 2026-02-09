from rest_framework import serializers
from main.validators import phone_validator

from main.models import *

class FeedbackSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(validators=[phone_validator])
    class Meta:
        model = Feedback
        fields = ["id", "user", "text", "phone"]
        read_only_fields = ["user"]
        

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forms
        fields = "__all__"

class OnlyFileFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forms
        fields = ["file"]