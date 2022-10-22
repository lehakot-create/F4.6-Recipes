from rest_framework import serializers

from .models import Recipes, Category


class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
