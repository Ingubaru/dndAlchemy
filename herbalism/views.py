from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Ingredient
from .generator import getIngredients


def ingredient_list(request):
	ingredients = Ingredient.objects.all().order_by('name')
	print(ingredients)
	return render(request, 'herbalism/ingredient_list.html', {'ingredients': ingredients})


def ingredient_detail(request, pk):
	ingredient = get_object_or_404(Ingredient, pk=pk)
	return render(request, 'herbalism/ingredient_detail.html', {'ingredient': ingredient})


def generator_menu(request):
	return render(request, 'herbalism/generator_menu.html')


def generator_result(request, region):
	ingredientsList = getIngredients(region)
	if   len(ingredientsList) == 1: ingredients = Ingredient.objects.filter(name__contains=ingredientsList[0])
	if   len(ingredientsList) == 1: ingredients = Ingredient.objects.filter(name__contains=ingredientsList[0])
	elif len(ingredientsList) == 2: ingredients = Ingredient.objects.filter(name__contains=ingredientsList[0]) | Ingredient.objects.filter(name__contains=ingredientsList[1])
	elif len(ingredientsList) == 3: ingredients = Ingredient.objects.filter(name__contains=ingredientsList[0]) | Ingredient.objects.filter(name__contains=ingredientsList[1]) | Ingredient.objects.filter(name__contains=ingredientsList[2])
	elif len(ingredientsList) == 4: ingredients = Ingredient.objects.filter(name__contains=ingredientsList[0]) | Ingredient.objects.filter(name__contains=ingredientsList[1]) | Ingredient.objects.filter(name__contains=ingredientsList[2]) | Ingredient.objects.filter(name__contains=ingredientsList[3])
	elif len(ingredientsList) == 5: ingredients = Ingredient.objects.filter(name__contains=ingredientsList[0]) | Ingredient.objects.filter(name__contains=ingredientsList[1]) | Ingredient.objects.filter(name__contains=ingredientsList[2]) | Ingredient.objects.filter(name__contains=ingredientsList[3]) | Ingredient.objects.filter(name__contains=ingredientsList[4])
	elif len(ingredientsList) == 6: ingredients = Ingredient.objects.filter(name__contains=ingredientsList[0]) | Ingredient.objects.filter(name__contains=ingredientsList[1]) | Ingredient.objects.filter(name__contains=ingredientsList[2]) | Ingredient.objects.filter(name__contains=ingredientsList[3]) | Ingredient.objects.filter(name__contains=ingredientsList[4]) | Ingredient.objects.filter(name__contains=ingredientsList[5])
	elif len(ingredientsList) == 7: ingredients = Ingredient.objects.filter(name__contains=ingredientsList[0]) | Ingredient.objects.filter(name__contains=ingredientsList[1]) | Ingredient.objects.filter(name__contains=ingredientsList[2]) | Ingredient.objects.filter(name__contains=ingredientsList[3]) | Ingredient.objects.filter(name__contains=ingredientsList[4]) | Ingredient.objects.filter(name__contains=ingredientsList[5]) | Ingredient.objects.filter(name__contains=ingredientsList[6])
	elif len(ingredientsList) == 8: ingredients = Ingredient.objects.filter(name__contains=ingredientsList[0]) | Ingredient.objects.filter(name__contains=ingredientsList[1]) | Ingredient.objects.filter(name__contains=ingredientsList[2]) | Ingredient.objects.filter(name__contains=ingredientsList[3]) | Ingredient.objects.filter(name__contains=ingredientsList[4]) | Ingredient.objects.filter(name__contains=ingredientsList[5]) | Ingredient.objects.filter(name__contains=ingredientsList[6]) | Ingredient.objects.filter(name__contains=ingredientsList[7])
	elif len(ingredientsList) == 9: ingredients = Ingredient.objects.filter(name__contains=ingredientsList[0]) | Ingredient.objects.filter(name__contains=ingredientsList[1]) | Ingredient.objects.filter(name__contains=ingredientsList[2]) | Ingredient.objects.filter(name__contains=ingredientsList[3]) | Ingredient.objects.filter(name__contains=ingredientsList[4]) | Ingredient.objects.filter(name__contains=ingredientsList[5]) | Ingredient.objects.filter(name__contains=ingredientsList[6]) | Ingredient.objects.filter(name__contains=ingredientsList[7]) | Ingredient.objects.filter(name__contains=ingredientsList[8])
	return render(request, 'herbalism/generator_result.html', {'ingredients': ingredients})
