from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.views import get_or_create_cart
from .models import Order, OrderItem


@login_required
def checkout(request):
    cart = get_or_create_cart(request)
    if not cart.items.exists():
        messages.warning(request, 'Your cart is empty.')
        return redirect('cart:detail')

    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            total_amount=cart.total_price,
            full_name=request.POST['full_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            city=request.POST['city'],
            state=request.POST['state'],
            pincode=request.POST['pincode'],
            payment_method=request.POST.get('payment_method', 'cod'),
        )
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                product_name=item.product.name,
                price=item.product.final_price,
                quantity=item.quantity,
            )
            # Reduce stock
            item.product.stock -= item.quantity
            item.product.save()

        cart.items.all().delete()
        messages.success(request, f'Order #{order.id} placed successfully!')
        return redirect('orders:order_detail', order_id=order.id)

    context = {'cart': cart, 'user': request.user}
    return render(request, 'orders/checkout.html', context)


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})
