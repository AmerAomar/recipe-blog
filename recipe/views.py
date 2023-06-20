from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import recipe


class recipeListView(ListView):
    template_name = "recipe/recipe-list.html"
    model = recipe


class recipeDetailView(DetailView):
    template_name = "recipe/recipe-detail.html"
    model = recipe


class recipeCreateView(CreateView):
    template_name = "recipe/recipe-create.html"
    model = recipe
    fields = ['name', 'cheff','ingredients','steps']
    success_url = reverse_lazy("recipe_list")


class recipeUpdateView(UpdateView):
    template_name = "recipe/recipe-update.html"
    model = recipe
    fields = ['name', 'cheff','ingredients','steps']
    success_url = reverse_lazy("recipe_list")


class recipeDeleteView(DeleteView):
    template_name = "recipe/recipe-delete.html"
    model = recipe
    success_url = reverse_lazy("recipe_list")
