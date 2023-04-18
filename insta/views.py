from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

class HomeView(View):
    def get(self, request):
        return HttpResponse('Hello World with class!')

def home(request):
    return HttpResponse('Hello World!')

def redirectview(request):
    return redirect('home-name')

def redirecthomeclass(request):
    return redirect('home-class')
