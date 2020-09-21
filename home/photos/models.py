from django.db import models

# Create your models here.


class Photo():
    image = models.ImageField(upload_to='images/', verbose_name='照片')
    name = models.TextField(verbose_name='照片名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '照片集'
