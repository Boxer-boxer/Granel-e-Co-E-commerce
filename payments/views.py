from django.shortcuts import render, get_object_or_404
from .models import Order
from users.models import Cart

from datetime import datetime
from string import ascii_uppercase
from random import randint

from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.
date = str(datetime.now())[:10].split('-')
hour = str(datetime.now())[11:16].split(':')
order_id = ''.join(date)+''.join(hour)+ascii_uppercase[randint(0,20)]+ascii_uppercase[randint(0,20)]+str(randint(0,100))+str(randint(0,100))+'Order'

class OrderCreateView(CreateView):

	model = Order
	fields = ['nome_completo', 
			'email', 
			'rua', 
			'andar', 
			'numero', 
			'localidade', 
			'distrito', 
			'codigo_postal_1', 
			'codigo_postal_2'
			]


	def get_context_data(self, **kwargs):

		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context = super(OrderCreateView, self).get_context_data(**kwargs)
		context['cart'] = cart_obj
		return context

	def form_valid(self, form):

		cart_obj, new_obj = Cart.objects.new_or_get(self.request)

		self.object = form.save(commit=False)
		if self.request.user.is_authenticated:
			self.object.user = self.request.user
		else:
			self.object.user= User.objects.get(username='DummyUser')
		self.object.cart = cart_obj
		self.object.order_id = order_id
		self.object.total = cart_obj.subtotal + 5
		self.object.save()


		return HttpResponseRedirect(self.get_success_url())


def OrderDetailView(request, slug):

	order = get_object_or_404(Order, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	for product in cart_obj.products.all():
		order.objects = product
	template = 'payments/order-detail.html'

	context = {
		'order': order,
		'cart':cart_obj,
		}

	return render(request, template, context)
