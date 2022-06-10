from rest_framework import serializers
from .models import *


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('name',)


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleData
        fields = ('name', 'color', 'model', 'registration_no', 'category')


class VehicleListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = VehicleData
        fields = ('name', 'color', 'model', 'registration_no', 'category')
