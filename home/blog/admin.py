from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Config, ConfigAdmin)
admin.site.register(Link, LinkAdmin)
