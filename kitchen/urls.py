from django.urls import path

from .views import Index, CreateRecipeView, DetailRecipeView, DeleteRecipeView, UpdateRecipeView


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('create/', CreateRecipeView.as_view(), name='create'),
    path('detail/<int:pk>/', DetailRecipeView.as_view(), name='detail'),
    path('update/<int:pk>/', UpdateRecipeView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteRecipeView.as_view(), name='delete'),
]