from news.models import News
from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["id", "title", "date"]


class OneNewsSerilizer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
