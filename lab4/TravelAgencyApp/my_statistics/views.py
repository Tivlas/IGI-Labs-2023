from django.shortcuts import render
from django.db.models import Sum, F
from django.db.models import Count
from django.db.models.functions import ExtractYear
from travel.models import Trip
from order.models import Order
from login.models import MyUser


def statistics(request):
    clients = MyUser.objects.order_by('last_name', 'first_name')
    client_data = []

    for client in clients:
        orders = client.order_set.all()
        total_sales = orders.annotate(
            total_cost=Sum(F('items__quantity') * F('items__cost'))
        ).aggregate(total_sales=Sum('total_cost'))['total_sales']
        client_data.append(
            {'client': client, 'orders': orders, 'total_sales': total_sales})

    context = {'client_data': client_data}
    return render(request, 'statistics.html', context)
