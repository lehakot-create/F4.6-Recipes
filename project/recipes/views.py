from rest_framework import generics

from .models import Recipes, Category
from .serializers import RecipesSerializer, CategorySerializer


class RecipesList(generics.ListAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
