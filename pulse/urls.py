from django.urls import path
from . import views

urlpatterns = [
	path('', views.pulse, name='acceuil'),
	path('direct', views.pulse, name='direct'),
]
