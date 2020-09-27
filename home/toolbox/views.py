from django.shortcuts import render
from django.views.generic import View
from django.http.request import HttpRequest
# Create your views here.


class ToolBoxIndex(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        return render(request=request, template_name="toolbox/index.html")
