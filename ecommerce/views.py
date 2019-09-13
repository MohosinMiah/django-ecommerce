from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    courses = ("PHP ","JAVA "," PYTHON")
    return render(request,'home.html')



def index(request):
    courses = ("PHP ","JAVA "," PYTHON")
    return HttpResponse(courses) 