from django.contrib import admin
from .models import Topic
from .models import Cat

admin.site.register(Topic) # Управление моделью должно осущество=лятся через административный сайт
admin.site.register(Cat)

# Register your models here.
