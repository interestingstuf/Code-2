from importlib.resources import path
import mimetypes

from unittest.mock import patch
from django.shortcuts import render
from django.http import HttpResponse, response
from .forms import formupload
from .functions import handle_uploaded_file
# Create your views here.
def home(request):
    return HttpResponse("Hi There This Is Parth Here And you Are Seeing The Parth Website")
def home1(request):
    return HttpResponse("Hi this is home 1 my another webpage")    
def page1(request):
    return render(request, "parth_app/Links.html")   
def home2(request):
   return render(request, "parth_app/Slide_ShowJava.html")   
def msfspage(request):
   return render(request, "parth_app/MSFSPage.html")   
def xplanepage(request):
   return render(request, "parth_app/X-PlanePage.html") 
def flightgearpage(request):
   return render(request, "parth_app/Flightgear.html")   
def acropage(request):
   return render(request, "parth_app/Acrosim.html")        
def getpdf(request):
   filepath="parth_app/static/parth_app/media/Test.pdf"
   path=open(filepath,"rb")
   mime_type, _ =mimetypes.guess_type(filepath)
   response=HttpResponse(path,content_type=mime_type)
   return response
def uploading1(request):
   if request.method=="POST":
      student=formupload(request.POST,request.FILES)
      if student.isvalid():
         handle_uploaded_file(request.FILES["File"] )
         return HttpResponse("File Uploaded Succesfully")
   else:
      student=formupload()
   return render(request,"parth_app/Downloadpdf.html",{"form":student})


def downloadpdfs(request):
   return render(request, "parth_app/Downloadpdf.html")       
def contact(request):
   return render(request, "parth_app/Contactme.html")           

      
           
   
        
   