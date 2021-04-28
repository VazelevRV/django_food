from django.shortcuts import render
from django_food_main.models import Dish


# Create your views here.
def dish_info(request, pk):
    dish = Dish.objects.get(pk=pk)
    return render(request, 'dish.html', context={'dish': dish})
