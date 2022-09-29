from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
# Create your views here.

def index(request):
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

def spanish(request):
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'spanish.html')

def french(request):
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'french.html')

def german(request):
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'german.html')

def chinese(request):
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'chinese.html')


#,{},context_instance=RequestContext(request)
