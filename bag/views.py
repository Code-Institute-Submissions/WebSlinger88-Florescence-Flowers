from django.shortcuts import render


def view_bag(request):
    """ Renders shopping bag page """

    return render(request, "bag/bag.html")
