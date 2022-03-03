from django.shortcuts import render, get_object_or_404
from .models import Ingredient


def ingredient_list(request):
	ingredients = Ingredient.objects.all().order_by('rarity')
	return render(request, 'herbalism/ingredient_list.html', {'ingredients': ingredients})


def ingredient_detail(request, pk):
	ingredient = get_object_or_404(Ingredient, pk=pk)
	return render(request, 'herbalism/ingredient_detail.html', {'ingredient': ingredient})