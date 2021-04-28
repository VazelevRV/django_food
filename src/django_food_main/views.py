from django.shortcuts import render, redirect
from .models import Category, Dish, Event
from .forms import ReservationForm
# Create your views here.


def main(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    events = Event.objects.filter(is_visible=True)

    special_categories = Category.objects.filter(is_visible=True, is_special=True).order_by('category_order')
    for category in special_categories:
        category.dishes = Dish.objects.filter(category=category.pk)

    categories = Category.objects.filter(is_visible=True, is_special=False).order_by('category_order')
    for category in categories:
        category.dishes = Dish.objects.filter(category=category.pk)

    reservation_form = ReservationForm()

    return render(request, 'index.html',
                  context={'categories': categories, 'special_categories': special_categories, 'events': events, 'form': reservation_form})
