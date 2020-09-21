import json
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    data={
        "status":"ok"
    }
    return HttpResponse(content=json.dumps(data), content_type="application/json")

