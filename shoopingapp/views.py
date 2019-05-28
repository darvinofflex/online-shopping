from django.shortcuts import render, get_object_or_404, redirect
from . models import Category, Product
from . forms import CategoryForm, ProductForm, UserForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, 'shoopingapp/index.html', {'products': products})

def detail(request,Product_id ):
    product = get_object_or_404(Product)
    return render(request, 'shoopingapp/detail.html', {'product': product})


def cancel_order(request, product_id, category_id):
    product = get_object_or_404(Product, pk=product_id)
    category = get_object_or_404(product.category_set, pk=product_id)
    category.delete()
    context = {'product': product,
               'message': 'Order Cancelled!'
               }
    return render(request, 'shoopingapp/detail.html', context)

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)

    return render(request, 'shoopingapp/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                products = Product.objects.all(user=request.user)
                return render(request, 'shoopingapp/index.html', {'products': products})
    return render(request, 'shoopingapp/login.html')


def logout_user(request):
    logout(request)
    return redirect('shoopingapp:login')

def add_item(request, product_id):
    form = ProductForm(request.POST or None)
    product = get_object_or_404(Product, pk=product_id)
    item = form.save(commit=False)
    item.product = product
    item.save()
    form = ProductForm()
    return render(request, 'shoopingapp/add_item.html', {'form': form})


