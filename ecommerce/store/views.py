from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Avg
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Product, Category, Review


def home(request):
    featured_products = Product.objects.filter(available=True, featured=True)[:8]
    categories = Category.objects.all()[:6]
    latest_products = Product.objects.filter(available=True)[:8]
    context = {
        'featured_products': featured_products,
        'categories': categories,
        'latest_products': latest_products,
    }
    return render(request, 'store/home.html', context)


def product_list(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    category_slug = request.GET.get('category')
    search_query = request.GET.get('q', '')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    sort_by = request.GET.get('sort', '-created_at')

    selected_category = None
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=selected_category)

    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    sort_options = {
        'price_asc': 'price',
        'price_desc': '-price',
        'name': 'name',
        '-created_at': '-created_at',
    }
    products = products.order_by(sort_options.get(sort_by, '-created_at'))

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'search_query': search_query,
        'sort_by': sort_by,
    }
    return render(request, 'store/product_list.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    reviews = product.reviews.all()
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    related_products = Product.objects.filter(
        category=product.category, available=True
    ).exclude(id=product.id)[:4]

    user_review = None
    if request.user.is_authenticated:
        user_review = reviews.filter(user=request.user).first()

    context = {
        'product': product,
        'reviews': reviews,
        'avg_rating': round(avg_rating, 1),
        'related_products': related_products,
        'user_review': user_review,
    }
    return render(request, 'store/product_detail.html', context)


@login_required
def add_review(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        Review.objects.update_or_create(
            product=product,
            user=request.user,
            defaults={'rating': rating, 'comment': comment}
        )
        messages.success(request, 'Your review has been submitted!')
    return __import__('django.shortcuts', fromlist=['redirect']).redirect('store:product_detail', slug=slug)
