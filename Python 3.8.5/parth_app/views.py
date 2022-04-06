from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hi There This Is Parth Here And you Are Seeing The Parth Website")
def home1(request):
    return HttpResponse("Hi this is home 1 my another webpage")    
def page1(request):
    return render(request, "parth_app/Links.html")   
def home2(request):
   return render(request, "parth_app/Websitefront.html")   
