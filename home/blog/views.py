from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse
from .models import Article

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. BLOG.")


class ArticleList(TemplateView):
    template_name = "article_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()
        return context


class ArticleView(TemplateView):
    template_name = "article.html"

    def get(self, request, *args, **kwargs):
        pass
