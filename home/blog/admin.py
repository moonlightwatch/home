from django.contrib import admin

from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'create_time', 'is_draft')


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'sub_title', 'icon_url')


class ConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')


# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Config, ConfigAdmin)
admin.site.register(Link, LinkAdmin)
