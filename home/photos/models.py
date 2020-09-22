from django.contrib import admin
from django.db import models
from django.utils.html import format_html
import urllib
# Create your models here.


class Photo(models.Model):
    image = models.ImageField(upload_to='images/', verbose_name='照片')
    name = models.TextField(verbose_name='照片名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def 预览(self):
        html = f'<img src="{self.image.url}" height="96px">'
        return format_html(html)

    def markdown(self):
        url = urllib.parse.unquote(self.image.url)
        return f"![{self.name}]({url})"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '照片集'


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_time', '预览', 'url')
