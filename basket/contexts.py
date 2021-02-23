from decimal import Decimal
from django.conf import settings


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENT / 100)
        almost_free_delivery = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        almost_free_delivery = 0

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'product_count': product_count,
        'total': total,
        'delivery': delivery,
        'free_delivery_delta': almost_free_delivery,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
