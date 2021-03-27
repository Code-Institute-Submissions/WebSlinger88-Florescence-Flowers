from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponse
from .forms import ProductForm, ReviewForm
from django.db.models import Q, Avg
from django.db.models.functions import Lower

from .models import (
    Product, Category, Colour, Occasion, ProductReview, ProductRating)


def all_products(request):
    """ A view showing all flowers, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    colours = None
    occasions = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'colour' in request.GET:
            colours = request.GET['colour'].split(',')
            products = products.filter(colour__name__in=colours)
            colours = Colour.objects.filter(name__in=colours)

        if 'occasion' in request.GET:
            occasions = request.GET['occasion'].split(',')
            products = products.filter(occasion__name__in=occasions)
            occasions = Occasion.objects.filter(name__in=occasions)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_colours': colours,
        'current_occasions': occasions,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual flowers' details """

    product = get_object_or_404(Product, pk=product_id)
    reviews = ProductReview.objects.filter(product=product)
    ratings = ProductRating.objects.filter(product=product)
    form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'ratings': ratings,
        'form': form,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add new flowers to the website """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry! \
            Only Florescence staff can use this function.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added new flowers!')
            return redirect(reverse('add_product'))
        else:
            messages.error(
                request, 'Failed to add flowers. Please check form.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit flowers within the website """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry! \
            Only Florescence staff can use this function.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated flowers!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Oh no! You failed to edit the selected flowers. \
                 Please check form.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete flowers from the website """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry! \
            Only Florescence staff can use this function.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Flowers have been successfully deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """Add a review and rating"""

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        product = ProductReview(pk=product_id)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = Product(pk=product_id)
            form.save()
            rating = ProductRating(
                product=product, rating=request.POST['rating'], review=review)
            rating.save()
            set_rating(product)
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('product_details', args=[product_id]))
        else:
            messages.error(request,
                           ('Failed to add review.'
                            'Please ensure the form is valid.'))

    return redirect(reverse('product_details', args=[product_id]))


@login_required
@require_POST
def update_review(request, review_id, rating_id):
    # Update User Reivew

    try:
        updated_review = request.POST['content']
        updated_rating = request.POST['rating']
        review = get_object_or_404(ProductReview, pk=review_id)
        rating = get_object_or_404(ProductRating, pk=rating_id)
        product = get_object_or_404(Product, pk=rating.product_id)
        if review.author == request.user:
            review.content = updated_review
            review.save()
            rating.rating = updated_rating
            rating.save()
            set_rating(product)
            return JsonResponse({'updated_rating': updated_rating, })
        else:
            return HttpResponse(status=403)

    except Exception as e:
        return HttpResponse(content=e, status=403)


@login_required
def delete_review(request, review_id):
    # Delete User Review

    try:
        review = get_object_or_404(ProductReview, pk=review_id)
        product = get_object_or_404(Product, pk=review.product_id)
        review.delete()
        set_rating(product)
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(content=e, status=404)


def set_rating(product):
    # Set User Rating
    rating = ProductRating.objects.filter(product=product)
    if rating.exists():
        product.avg_rating = ProductRating.objects.filter(product=product)\
            .aggregate(Avg('rating'))['rating__avg']
        product.save(update_fields=['avg_rating'])
    else:
        product.avg_rating = 0
        product.save()
