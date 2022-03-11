from random import randint
from django.shortcuts import render, get_object_or_404
from .models import Ingredient, Potion
from .generator import getIngredients


def ingredient_list(request):
	ingredients = Ingredient.objects.all().order_by('name')
	return render(request, 'herbalism/ingredient_list.html', {'ingredients': ingredients})


def ingredient_detail(request, pk):
	ingredient = get_object_or_404(Ingredient, pk=pk)
	return render(request, 'herbalism/ingredient_detail.html', {'ingredient': ingredient})


def generator_menu(request):
	return render(request, 'herbalism/generator_menu.html')


def generator_result(request, region):
	ingredientsList = getIngredients(int(region))
	ingredients = []
	for i in ingredientsList:
		ingredients.append(Ingredient.objects.filter(name__contains=i))
	return render(request, 'herbalism/generator_result.html', {'ingredients': ingredients})


def potion_list(request):
	potions = Potion.objects.all().order_by('price')
	return render(request, 'herbalism/potion_list.html', {'potions': potions})


def potion_detail(request, pk):
	potion = get_object_or_404(Potion, pk=pk)
	return render(request, 'herbalism/potion_detail.html', {'potion': potion})


def seller(request, ingr_type):
	if   ingr_type == '0': base_price = 8
	elif ingr_type == '1': base_price = 20
	elif ingr_type == '2': base_price = 50 
	else 		       : base_price = 0
	if   ingr_type == '0': modifier = 10
	elif ingr_type == '1': modifier = 0
	elif ingr_type == '2': modifier = -10 
	else 		       : modifier = 0
	factor_scale = randint(1, 100) + modifier
	if   factor_scale < 21: factor = 0.1
	elif factor_scale < 41: factor = 0.2
	elif factor_scale < 81: factor = 0.5
	elif factor_scale > 80: factor = 1.0
	price = base_price * factor
	return render(request, 'herbalism/seller.html', {'price': price})