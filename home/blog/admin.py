from django.contrib import admin

from .models import Tag, Category, Article, Config

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Config)
admin.site.register(Link)
