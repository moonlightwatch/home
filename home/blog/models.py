from django.db import models

# Create your models here.


class Tag(models.Model):
    '''
    标签
    '''
    name = models.CharField(max_length=200, verbose_name='标签名称')

    def __str__(self):
        return self.name


class Category(models.Model):
    '''
    分类
    '''
    name = models.CharField(max_length=200, verbose_name='分类名称')

    def __str__(self):
        return self.name


class Article(models.Model):
    '''
    文章
    '''
    title = models.CharField(max_length=200, verbose_name='标题')
    content = models.TextField(verbose_name='正文')
    is_draft = models.BooleanField(verbose_name='是否草稿')
    category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL, verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    edit_time = models.DateTimeField(auto_now_add=True, verbose_name='最后编辑时间')

    def __str__(self):
        return self.title

class Link(models.Model):
    '''
    友链
    '''
    title = models.CharField(max_length=200, verbose_name='标题')
    url = models.CharField(max_length=2048, verbose_name='地址')
    icon_url = models.CharField(max_length=2048, verbose_name='图标地址')
    sub_title = models.CharField(max_length=200, verbose_name='副标题')

class Config(models.Model):
    '''
    配置
    '''
    name = models.CharField(max_length=200, verbose_name='配置项')
    value = models.TextField(verbose_name='配置内容')

    def __str__(self):
        return self.name
