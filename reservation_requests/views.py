from django.core.paginator import Paginator
from django.shortcuts import render
from django_food_main.models import Reservation
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
@login_required(login_url='/login/')
@user_passes_test(lambda u: u.groups.filter(name='manager').exists() or u.is_staff, login_url='/login/')
def reservations_view(request):

    messages = Reservation.objects.filter(is_processed=False).order_by('send_date')
    paginator = Paginator(messages, 2)
    page = request.GET.get('page')
    messages_page = paginator.get_page(page)
    return render(request, 'reservations.html', context={'items': messages_page})
