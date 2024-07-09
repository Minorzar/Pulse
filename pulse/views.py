from django.shortcuts import render

# Create your views here.

def pulse(request):
	return render(request, 'index.html')

def calendar(request):
	return render(request, 'calendar.html')
