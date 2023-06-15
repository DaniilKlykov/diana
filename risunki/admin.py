from django.contrib import admin
from .models import Risunki


class RisunkiAdmin(admin.ModelAdmin):
    #  поля которые отображаются в админке
    list_display = ('pk', 'name', 'author', 'canvas', 'paints', 'size')
    # интерфейс поиска
    search_fields = ('name',)
    # фильтрация по имени и автору
    list_filter = ('name', 'author',)


admin.site.register(Risunki, RisunkiAdmin)
