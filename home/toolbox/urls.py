from django.urls import path

from . import views

urlpatterns = [
    path('', views.ToolBoxIndex.as_view(), name='toolbox_index'),
]
