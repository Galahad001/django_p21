"""Определяет схемы URL для my_blog"""
from django.urls import path # path-неоюходим для связывания url с представлениями

from . import views # . приказывает питону импортировать представления из каталого в котором находится текущий модуль urls

urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),  # Вызов функции path с 3 аргументами 1-содержит строку позволяющую определить текщий запрос. 2-определяет вызываемую функцию. 3-Имя этой схемы 
    #Страница для всех тем
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]