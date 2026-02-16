from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.

def hello(request):
    return HttpResponse( "hello world")

class HelloEthiopia(View):
    def get(self, request):
        return HttpResponse(request, "hello ethiopia")


