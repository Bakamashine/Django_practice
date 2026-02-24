from rest_framework import serializers

from products.models import Category, Product


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "img"]


class ProductSerializersOne(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "img"]


class CategorySerializersOne(serializers.ModelSerializer):
    products = ProductSerializers(many=True)

    class Meta:
        model = Category
        # fields = ['id','name', 'description', 'img', 'products']
        fields = "__all__"


class OnlyFileProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["file"]
