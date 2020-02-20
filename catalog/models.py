from django.db import models


class ProdutoGranel(models.Model):
	
	tamanhos = [
	('0.50kg', '0.50kg'),
	('1.00kg', '1.00kg'),
	('1.50kg', '1.50kg'),
	]

	types = [
		('Granel' , 'Granel'),
		('Individuais' , 'Individuais')
	]

	name = models.CharField(max_length=50)
	description = models.TextField(max_length=500)
	price = models.FloatField()
	image= models.ImageField(upload_to="media")
	date= models.DateTimeField(auto_now_add=True)
	size = models.CharField(max_length=10, choices=tamanhos, default='0.50kg')
	product_type = models.CharField(max_length=50, choices=types)

	def __str__(self):
		return self.name

