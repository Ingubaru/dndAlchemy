from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.generator_menu, name='generator_menu'),
	path('ingredient_list', views.ingredient_list, name='ingredient_list'),
	path('generator_menu', views.generator_menu, name='generator_menu'),
	re_path(r'^ingredient/(?P<pk>[0-9]+)/$', views.ingredient_detail, name="ingredient_detail"),
]