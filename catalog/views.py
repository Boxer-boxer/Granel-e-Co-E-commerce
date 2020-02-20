from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import ProdutoGranel
from users.models import Cart

# Create your views here.
def test(request):	

	cart_obj, new_obj = Cart.objects.new_or_get(request)
	products = ProdutoGranel.objects.all().order_by('-date')[:12]
	
	context = {
		'products': products,
		'cart':cart_obj
		}
	
	return render(request, 'catalog/test.html', context)

def home(request):
	
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	products = ProdutoGranel.objects.all().order_by('-date')[:12]
	
	context = {
		'products': products,
		'cart':cart_obj
		}
		
	return render(request, 'catalog/home.html', context)

def catalog(request):

	produtos = ProdutoGranel.objects.all().order_by('-date')
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	
	paginator = Paginator(produtos, 21)

	page = request.GET.get('page')
	products = paginator.get_page(page)

	context = {
		'products':products,
		'cart':cart_obj
	}

	return render(request, 'catalog/catalog.html', context)

def detail(request, pk):
	product = ProdutoGranel.objects.get(id=pk)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	context = {
		'product':product,
		'cart':cart_obj
	}
	return render(request, 'catalog/detail.html', context)



