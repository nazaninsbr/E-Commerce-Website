from django.shortcuts import render
from django.http import HttpResponse, Http404 
from datetime import datetime
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

def home(request):
	now = datetime.now()
	return HttpResponse("<html><body>Hello, World!, time: {}</body></html>".format(now))

def product(request, product_id):
	raise PermissionDenied 
	#return render(request, 'product.html', {'now':datetime.now()})