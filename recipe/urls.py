from django.urls import path
from .views import recipeListView, recipeDetailView, recipeCreateView, recipeUpdateView, recipeDeleteView

urlpatterns = [
    path('recipe/', recipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/', recipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/create/', recipeCreateView.as_view(), name='recipe_create'),
    path('recipe/<int:pk>/update/', recipeUpdateView.as_view(), name='recipe_update'),
    path('recipe/<int:pk>/delete/', recipeDeleteView.as_view(), name='recipe_delete'),
]