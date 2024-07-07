from django.urls import path
from . import views

urlpatterns = [
	path('', views.pulse, name='acceuil'),
	path('diffusion', views.pulse, name='diffusion'),
	path('direct', views.pulse, name='direct'),
]
