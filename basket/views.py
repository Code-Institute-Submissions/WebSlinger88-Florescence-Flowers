from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product


def view_basket(request):
    """ Renders shopping basket page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Adds quantity of flowers to shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity to ({basket[item_id]})')
    else:
        basket[item_id] = quantity
        messages.success(
            request, f'You have added {product.name} to your basket.')

    request.session['basket'] = basket
    return redirect(redirect_url)


def update_basket(request, item_id):
    """ Change quantity of flowers within basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity') or 0)
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to ({basket[item_id]})')
    else:
        basket.pop(item_id)
        messages.info(
            request, f'You have removed {product.name} from your basket.')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_flowers(request, item_id):
    """ Remove selected flowers from basket """

    try:
        product = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})

        basket.pop(item_id)
        messages.info(
            request, f'You have removed {product.name} from your basket.')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing flowers: {e}')
        return HttpResponse(status=500)
