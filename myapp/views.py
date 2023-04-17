from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request, username):
    print(type(username))
    return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
    return HttpResponse('About')

def index(request):
    return HttpResponse('Page Index')
    