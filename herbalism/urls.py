from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.ingredient_list, name='ingredient_list'),
	re_path(r'^ingredient/(?P<pk>[0-9]+)/$', views.ingredient_detail, name="ingredient_detail"),
]