
from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse
import json
import jieba.analyse
# Create your views here.


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="api/index.html")


class StatusView(View):
    def get(self, request, *args, **kwargs):
        status = {
            "status": "ok"
        }
        return JsonResponse(data=status, json_dumps_params={"ensure_ascii": False})


class MakeKeywordsView(View):
    def get(self, request, *args, **kwargs):
        print(args)
        result = {
            "postdata": {
                "text": "xxxxx",
                "num": 10
            }
        }
        return JsonResponse(data=result, json_dumps_params={"ensure_ascii": False})

    def post(self, request, *args, **kwargs):
        data = {}
        result = {}
        try:
            data = json.loads(request.body.decode("utf8"))
        except:
            return JsonResponse(data=result, json_dumps_params={"ensure_ascii": False})

        text = data.get("text", "")
        num = data.get("num", 5)
        if not text:
            return JsonResponse(data=result, json_dumps_params={"ensure_ascii": False})
        result["keywords"] = jieba.analyse.textrank(
            sentence=text, topK=num, withWeight=False)
        return JsonResponse(data=result, json_dumps_params={"ensure_ascii": False})
