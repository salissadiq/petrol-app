from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)


	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name
    

class Sales(models.Model):
	user = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	amount = models.IntegerField(null=True, default=0)