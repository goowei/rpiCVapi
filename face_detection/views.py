from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
import datetime


# Create your views here.
class FaceDetection(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # working with variables in templates
        context = super().get_context_data(**kwargs)
        context["detectResult"] = datetime.datetime.now().strftime("%Y/%m/%d, %a, %I:%M %p")
        return context
    def detect(self):
        result = {
                "Success":False,
                "date":datetime.datetime.now().strftime("%Y/%m/%d, %a, %I:%M %p"),
            }
        return JsonResponse(result)