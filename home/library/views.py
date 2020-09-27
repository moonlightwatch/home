from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from .models import *
# Create your views here.

class BookList(ListView):
    template_name = "library/booklist.html"
    model = Book

class BookDetail(DetailView):
    template_name = "library/book.html"
    model = Book

class ChapterDetail(DetailView):
    template_name = "library/chapter.html"
    model = Chapter

class CategoryList(ListView):
    template_name = "library/category_list.html"
    model = Category


class CategoryDetail(DetailView):
    template_name = "library/category.html"
    model = Category

    def get_object(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        queryset = Category.objects.filter(pk=pk)
        obj = {}
        obj["category"] = queryset.get()
        obj["books"] = Book.objects.filter(category=obj["category"].id).order_by('-create_time')
        return obj
