from django.db import models
from users.models import Cart
from catalog.models import ProdutoGranel
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

from .utils import unique_slug


# Create your models here.

class Order(models.Model):

	DISTRITO = (
		('Aveiro', 'Aveiro'),
		('Beja', 'Beja'),
		('Braga', 'Braga'),
		('Bragança', 'Bragança'),
		('Castelo Branco', 'Castelo Branco'),
		('Coimbra', 'Coimbra'),
		('Évora', 'Évora'),
		('Faro', 'Faro'),
		('Guarda', 'Guarda'),
		('Leiria', 'Leiria'),
		('Lisboa', 'Lisboa'),
		('Portalegre', 'Portalegre'),
		('Porto', 'Porto'),
		('Santarém', 'Santarém'),
		('Setúbal', 'Setúbal'),
		('Viana do Castelo', 'Viana do Castelo'),
		('Vila Real', 'Vila Real'),
		('Viseu', 'Viseu'),
		('Ilha da Madeira', 'Ilha da Madeira'),
		('Ilha de Porto Santo', 'Ilha de Porto Santo'),
		('Ilha de Santa Maria', 'Ilha de Santa Maria'),
		('Ilha de São Miguel', 'Ilha de São Miguel'),
		('Ilha Terceira', 'Ilha Terceira'),
		('Ilha da Graciosa', 'Ilha da Graciosa'),
		('Ilha de São Jorge', 'Ilha de São Jorge'),
		('Ilha do Pico', 'Ilha do Pico'),
		('Ilha do Faial', 'Ilha do Faial'),
		('Ilha das Flores', 'Ilha das Flores'),
		('Ilha do Corvo', 'Ilha do Corvo'),
		)

	order_id = models.CharField(max_length=100, null=False, default="code_order")
	nome_completo = models.CharField(max_length=150, null=False)
	email = models.EmailField()
	rua = models.CharField(max_length=300, null=False)
	numero = models.CharField(max_length=300, null=False)
	andar = models.CharField(max_length=300, null=False)
	localidade = models.CharField(max_length=60, null=False, default = '')
	distrito = models.CharField(choices=DISTRITO, max_length=30, null=False, default = '') 
	morada = models.IntegerField(blank=True, null=True, default=0)
	codigo_postal_1 = models.IntegerField(blank=True, null=True, default=1000) #raise an error if codigo_postal != intenger
	codigo_postal_2 = models.IntegerField(blank=True, null=True, default=100)
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
	cart = models.ForeignKey(Cart, null=True, on_delete=models.SET_NULL)
	items = models.ForeignKey(ProdutoGranel, null=True, on_delete=models.SET_NULL)
	#items = models.CharField(max_length=500, null=False, default='') #, on_delete=models.SET_NULL)  #add items to the order, so we know what was being ordered
	total = models.IntegerField(blank=True, null=True)
	is_ordered = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True)
	
	slug = models.SlugField(max_length=100, default='')

	def get_absolute_url(self):
	 	return reverse('order-detail', kwargs={'slug':self.slug})

	def __str__(self):
		return self.order_id

def slug_save(sender, instance, *args, **kwargs):
	if instance.slug == '':
		instance.slug = unique_slug(instance, instance.order_id, instance.slug)

pre_save.connect(slug_save, sender=Order)