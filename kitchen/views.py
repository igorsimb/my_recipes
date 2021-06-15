from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse

from .models import Recipe
from .forms import RecipeCreateForm


class Index(ListView):
    model = Recipe
    template_name = 'kitchen/index.html'
    context_object_name = 'recipes'


class CreateRecipeView(CreateView):
    form_class = RecipeCreateForm
    template_name = 'kitchen/create.html'
    context_object_name = 'recipes'
    success_url = '/'


class DetailRecipeView(DetailView):
    model = Recipe
    template_name = 'kitchen/detail.html'
    context_object_name = 'recipes'


class UpdateRecipeView(UpdateView):
    model = Recipe
    template_name = 'kitchen/update.html'
    context_object_name = 'recipes'
    fields = '__all__'
    # success_url = '/'

    def get_success_url(self):
        return reverse('detail', args=[self.object.pk])  # or args=(self.object.ok,) WITH A COMMA


class DeleteRecipeView(DeleteView):
    model = Recipe
    template_name = 'kitchen/delete.html'
    context_object_name = 'recipes'
    success_url = '/'


