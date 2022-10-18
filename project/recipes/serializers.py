from dataclasses import fields
from rest_framework import serializers

from .models import Recipes, Category


class RecipesSerializer(serializers.Serializer):
    class Meta:
        models = Recipes
        fields = '__all__'



class CategorySerializer(serializers.Serializer):
    class Meta:
        models = Category
        fields = '__all__'
