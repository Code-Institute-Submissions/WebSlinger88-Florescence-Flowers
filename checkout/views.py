from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(
            request, "You don't have any lovely flowers in your basket!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IUc8zBKhANMa3lShnMsLpY7yMBg0p5AjJvFPVBAE7ZXZbblpTnP6XjiYD0kH758a6Et7kZVM2VckpshaGnXjnQ700HO2R9oQ9',
        'client_secret': 'test.client_secret',
    }

    return render(request, template, context)
