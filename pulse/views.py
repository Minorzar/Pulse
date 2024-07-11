from django.shortcuts import render


# Create your views here.
def pulse(request):
	return render(request, 'index.html')
