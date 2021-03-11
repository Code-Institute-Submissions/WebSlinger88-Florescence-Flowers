from django import template

""" Calculates basket subtotal """

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
