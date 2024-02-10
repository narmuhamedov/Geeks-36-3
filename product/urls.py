from django.urls import path
from . import views

urlpatterns = [
    path('product_drinks/', views.ProductDrinksList.as_view(), name='drinks_list'),
    path('product_meals/', views.ProductMealsList.as_view(), name='meals_list'),
]
