from django.urls import path

from .views import RecipesList, CategoryList


urlpatterns = [
    path('recipes/', RecipesList.as_view()),
    path('category/', CategoryList.as_view()),
]