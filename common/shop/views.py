from django.shortcuts import render
from .models import Product,Category,Order

def product_list(request):
    categories=Category.objects.all()
    search_query=request.GET.get('search',None)
    if search_query:
        products=Product.objects.filter(title__icontains=search_query)
    else:
        products=Product.objects.all()
    return render(request, 'shop/product_list.html', context={'product_list': products, 'category_list': categories})

def product_detail(request,pk):
    categories=Category.objects.all()
    product=Product.objects.get(pk=pk)
    return render(request, 'shop/product_detail.html', context={'product': product, 'category_list': categories})


def category_detail(request,pk):
    categories=Category.objects.all()
    category=Category.objects.get(pk=pk)
    return render(request, 'shop/category_detail.html', context={'category': category, 'category_list': categories})

def save_order(request):
    categories=Category.objects.all()
    user_name=request.POST['user_name']
    user_email=request.POST['user_email']
    product_id=request.POST['product_id']
    order=Order()
    order.name=user_name
    order.email=user_email
    order.product=Product.objects.get(pk=product_id)
    order.save()
    return render(request, 'shop/save_order.html',context={'order': order, 'category_list': categories})

