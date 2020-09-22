from django.contrib import admin
from .models import *


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_time', '预览', 'markdown')

# Register your models here.


admin.site.register(Photo, PhotoAdmin)
