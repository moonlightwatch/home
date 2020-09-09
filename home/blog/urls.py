from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog_index'),
    path('articles/', views.ArticleList.as_view(), name='articles'),
    path('article/<int:pk>', views.ArticleDetail.as_view(), name='article'),

    path('tags/', views.TagList.as_view(), name='tags'),
    # path('tag/<int:pk>', views.TagDetail.as_view(), name='tag'),

    path('categories/', views.CategoryList.as_view(), name='categories'),
    path('category/<int:pk>', views.CategoryDetail.as_view(), name='category'),

    path('links/', views.LinkList.as_view(), name='links'),
]
