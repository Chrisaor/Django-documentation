from django.shortcuts import render

def index(request):
    return render(request, 'django_docu/index.html')

def tutorials(request):
    return render(request, 'tutorials/intro.html')