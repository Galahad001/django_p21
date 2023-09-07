from django.db import models

class Topic(models.Model):
    """Тема пользователя"""
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.text


class Cat(models.Model):
    """Информация изученая по теме"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Cats' # Приказывает Django использовать форму множественного числа при нахождении более одной записи

    def __str__(self):
        return f"{self.text[:50]}..."

# Create your models here.
