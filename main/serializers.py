from rest_framework import serializers

from main.models import *

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ["id", "user", "text", "phone"]
        read_only_fields = ["user"]
        

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forms
        fields = "__all__"