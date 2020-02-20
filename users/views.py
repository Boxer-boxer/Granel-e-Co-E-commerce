from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.http import HttpResponseRedirect

from .forms import UserRegisterForm
from .models import Cart
from catalog.models import ProdutoGranel

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username= username, password = raw_password)
			messages.success(request, f'A sua conta foi criada, {username}')
			return redirect('login')
	else:
		form = UserRegisterForm()

	context = {
		'form':form
	}

	return render(request, 'users/register.html', context)

def cart(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	context = {
	 	'cart': cart_obj
	}
	return render(request, 'users/cart.html', context)

def cart_update(request):

	product_id = request.POST.get('product_id')

	if product_id is not None:
		try:
			obj = ProdutoGranel.objects.get(id=product_id)
		except ProdutoGranel.DoesNotExist:
			return redirect('home') 

		cart_obj, new_obj = Cart.objects.new_or_get(request)

		if obj in cart_obj.products.all():
			cart_obj.products.remove(obj)
		else:
			cart_obj.products.add(obj)

	return redirect(request.META['HTTP_REFERER'])
	#return HttpResponseRedirect(request.path_info)
	#return redirect('catalog')
