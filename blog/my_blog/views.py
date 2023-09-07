from django.shortcuts import render

def index(request):
    """Домашняя страница"""
    return render(request, 'my_blog/index.html')

# Create your views here.
