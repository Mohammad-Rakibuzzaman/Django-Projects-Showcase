from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.


def hello_func(response):
      return HttpResponse("Hello from func")


class heloClass(View):
      def get(self, response):
            return HttpResponse("Hello from class")
