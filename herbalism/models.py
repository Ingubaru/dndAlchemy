from django.db import models


class Ingredient(models.Model):

	name = models.CharField(max_length=50)
	rarity = models.IntegerField(default=0)
	region = models.CharField(max_length=50)
	isMagic = models.BooleanField(default=False)
	difficult = models.IntegerField(default=0)
	effect = models.TextField(default='')
	description = models.TextField(default='')

	def __str__(self):
		return self.name


class Potion(models.Model):

	name = models.CharField(max_length=50)
	rarity = models.IntegerField(default=0)
	effect = models.TextField(default='')
	description = models.TextField(default='')

	def __str__(self):
		return self.name
