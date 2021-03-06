from django.db import models
# Create your models here.
class Stock(models.Model):
	ticker = models.CharField(max_length=10)

	def __str__(self):
		return self.ticker

class UpperLimit(models.Model):	
	highprice = models.FloatField(default=None)	

	def __float__(self):
		return self.highprice

class LowerLimit(models.Model):	
	lowprice = models.FloatField(default=None)

	def __float__(self):
		return self.lowprice