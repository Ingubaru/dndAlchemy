from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.generator_menu, name='generator_menu'),
	path('generator_menu', views.generator_menu, name='generator_menu'),
	re_path(r'^generator_result/(?P<region>[0-9]+)/$', views.generator_result, name='generator_result'),
	path('ingredient_list', views.ingredient_list, name='ingredient_list'),
	re_path(r'^ingredient/(?P<pk>[0-9]+)/$', views.ingredient_detail, name="ingredient_detail"),
	path('potion_list', views.potion_list, name='potion_list'),
	re_path(r'^potion/(?P<pk>[0-9]+)/$', views.potion_detail, name="potion_detail"),
]