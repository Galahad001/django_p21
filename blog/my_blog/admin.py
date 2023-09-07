from django.contrib import admin
from .models import Topic
from .models import Cat

# class Topic(admin.ModelAdmin):
#     list_display = ('id', 'text', 'date')
#     list_display_links = ('id', 'date')
#     search_fields = ('text', 'date')
#     list_filter = ('text')


# class CategoryAdmins(admin.ModelAdmin):
#     list_display = ('id', 'name', )
#     list_display_links = ('id', 'name')
#     search_fields = ('name',)

admin.site.register(Topic) # Управление моделью должно осущество=лятся через административный сайт
admin.site.register(Cat)

# Register your models here.
