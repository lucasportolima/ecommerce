from django.shortcuts import render

from .models import Product, Category

def product_list(request):
    context = {
        'product_list': Product.objects.all()
    }
    return render(request, 'catalog/product_list.html', context)

def category(request, slug):
    print(slug)
    category = Category.objects.get(slug=slug)
    context = {
        'current_category': category.name,
        'product_list': Product.objects.filter(category=category)
    }
    return render(request, 'catalog/product_list.html', context)