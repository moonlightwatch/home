from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name='library_index'),
    path('book/', views.BookDetail.as_view(), name="library_book"),
    path('chapter/<int:pk>', views.ChapterDetail.as_view(), name="library_chapter"),
    path('categories/', views.CategoryList.as_view(), name='library_categories'),
    path('category/<int:pk>', views.CategoryDetail.as_view(), name='library_category'),
]
