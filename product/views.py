from django.views import generic
from django.shortcuts import get_object_or_404
from . import models


class ProductDrinksList(generic.ListView):
    template_name = 'products/product_drinks_list.html'
    context_object_name = 'drinks_list'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter(tags__name='#напитки').order_by("-id")


class ProductMealsList(generic.ListView):
    template_name = 'products/product_meals_list.html'
    context_object_name = 'meals_list'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter(tags__name='#еда').order_by("-id")