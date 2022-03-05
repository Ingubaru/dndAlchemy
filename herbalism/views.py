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
	ingredientsList = getIngredients(int(region))
	ingredients = []
	for i in ingredientsList:
		ingredients.append(Ingredient.objects.filter(name__contains=i))
	return render(request, 'herbalism/generator_result.html', {'ingredients': ingredients})
