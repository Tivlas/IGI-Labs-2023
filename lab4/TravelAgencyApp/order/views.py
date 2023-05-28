from django.shortcuts import render
from .models import OrderItem
from cart.cart import Cart
from .models import Order
from django.core.exceptions import PermissionDenied


def create_order(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("Permission denied. Sign in first.")

    cart = Cart(request)
    if request.method == 'POST':
        order = Order.objects.create(client=request.user)

        for item in cart:
            OrderItem.objects.create(order=order,
                                     trip=item['trip'],
                                     cost=item['cost'],
                                     quantity=item['quantity'])
        cart.clear()
        return render(request, 'order_created.html')

    return render(request, 'create_order.html',
                  {'cart': cart})
