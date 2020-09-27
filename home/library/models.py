from django.db import models

# Create your models here.


class Category(models.Model):
    '''
    分类
    '''
    name = models.CharField(max_length=200, verbose_name='分类名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '书籍分类'

class Book(models.Model):
    '''
    书籍
    '''
    title = models.CharField(max_length=200, verbose_name='书名')
    author = models.CharField(max_length=200, verbose_name='作者')
    cover_img = models.ImageField(upload_to='bookimages/', verbose_name='封面')
    describ = models.CharField(max_length=2048, verbose_name='简介')
    create_time =  models.DateTimeField(auto_now_add=True, verbose_name='入库时间')
    category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL, verbose_name='分类')

    class Meta:
        verbose_name_plural = '书籍'


class Chapter(models.Model):
    '''
    章节
    '''
    title = models.CharField(max_length=200, verbose_name='书名')
    serial_num = models.IntegerField(verbose_name='序号')
    content = models.TextField(verbose_name='内容')
    book = models.ForeignKey(
        Book, null=False, on_delete=models.PROTECT, verbose_name='所属书籍')

    class Meta:
        verbose_name_plural = '章节'

