from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('status/', views.StatusView.as_view()),
    path('makekeywords/', views.MakeKeywordsView.as_view())
]
