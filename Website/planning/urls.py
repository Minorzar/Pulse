from django.urls import path
from . import views


urlpatterns = [
    path('diffusion', views.calendar, name='diffusion'),
]
