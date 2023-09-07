from django.shortcuts import render
from .models import Topic       # Импорт модели с нужными данными

def index(request):
    """Домашняя страница"""
    return render(request, 'my_blog/index.html')

def topics(request):        # Необходимый параметр request полученный от сервера
    """Выводит список тем"""
    topics = Topic.objects.order_by('date')      # Запрос к базе данных  на получение обьектов Topic, отсортированных по полю date
    context = {'topics': topics}                # Определяется контекст который передается шаблону. Ключ-это имя по которому в шаблонк можно получить значение
    return render(request, 'my_blog/topics.html', context)

# Create your views here.
