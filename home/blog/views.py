from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, TemplateView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article, Tag, Category, Link

# Create your views here.


def index(request):
    return HttpResponseRedirect(redirect_to="/blog/articles/")


class ArticleList(ListView):
    template_name = "blog/article_list.html"
    model = Article
    paginate_by = 10

    def get_queryset(self):  # 重写get_queryset方法
        return Article.objects.filter(is_draft=False).order_by('-create_time')


class ArticleDetail(DetailView):
    template_name = "blog/article.html"
    model = Article


class TagList(ListView):
    template_name = "blog/tag_list.html"
    model = Tag


class TagDetail(DetailView):
    template_name = "blog/tag.html"
    model = Tag


class CategoryList(ListView):
    template_name = "blog/category_list.html"
    model = Category


class CategoryDetail(DetailView):
    template_name = "blog/category.html"
    model = Category

    def get_object(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        queryset = Category.objects.filter(pk=pk)
        obj = {}
        obj["category"] = queryset.get()
        obj["articles"] = Article.objects.filter(
            is_draft=False, category=obj["category"].id).order_by('-create_time')
        return obj


class LinkList(ListView):
    template_name = "blog/link_list.html"
    model = Link
