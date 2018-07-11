from django.shortcuts import render
from .forms import OrderForm
from cart.cart import Cart
from .models import Order,OrderItem
# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            order=form.save()
            for item in cart:
              OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
              )
            cart.clear()
        return render(request,'cartcreated.html',{'order':order})
    else:
        form=OrderForm()
    return render(request,'cartcreate.html',{'form':form})


def my_orders(request):
    user=request.user
    temp = Order.objects.all().select_related('items')
    print(temp)
    obj=Order.objects.all()
    return render(request,'myorders.html')
