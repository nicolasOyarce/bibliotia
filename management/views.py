from django.contrib.auth.decorators import login_required
from django.core.files import File
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from accounts.models import Account
from category.forms import CategoryForm
from category.models import Category
from orders.models import Order
from store.forms import ProductForm
from store.models import Product


# Products
@login_required
def management_product(request):
    """
    View for management product
    """
    products = Product.objects.all()
    return render(request, 'management/products/products.html', {
        'products': products,
    })

@login_required
def product_add(request):
    """
    View for add product
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        
        if form.is_valid():  
            product = form.save(commit=False)
            
            image = request.FILES['image']
            product.image.save(image.name, File(image), save=True)

            product.save()
            return redirect('management:management_products')

    else:
        form = ProductForm()

    return render(request, 'management/products/product_add.html', {'form': form})

@login_required
def product_edit(request, id):
    product = Product.objects.get(id=id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save() 
            return redirect('management:management_products')
    
    else:
        form = ProductForm(instance=product)
        
    return render(request, 'management/products/product_edit.html', {
        'form': form,
        'product': product,
    })

@login_required
def product_delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('management:management_products') 

# Orders
@login_required
def management_order(request):
    orders = Order.objects.all()
    return render(request, 'management/orders/orders.html', {
        'orders': orders,
    })

# Users
@login_required
def management_users(request):
    """
    View for management users
    """
    users = Account.objects.all()
    return render(request, 'management/users/users.html', {
        'users': users,
    })

@login_required
def user_delete(request, id):
    """
    View for delete user
    """
    user = get_object_or_404(Account, id=id) 
    user.delete()
    return HttpResponseRedirect(reverse('management:management_users')) 





# Categories
@login_required
def management_categories(request):
    """
    View for management categories
    """
    categories = Category.objects.all()
    return render(request, 'management/categories/categories.html', {
        'categories': categories,
    })

@login_required
def category_add(request):
    """
    View for add category
    """
    form = CategoryForm()
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save() 
            return redirect('management:management_categories')
    else:
        form = CategoryForm()

    return render(request, 'management/categories/category_add.html', {
        'form': form
    })
    
@login_required
def category_edit(request, id):
    category = Category.objects.get(id=id)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save() 
            return redirect('management:management_categories')
    
    else:
        form = CategoryForm(instance=category)
        
    return render(request, 'management/categories/category_edit.html', {
        'form': form,
        'category': category,
    })
    
@login_required
def category_delete(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('management:management_categories')

