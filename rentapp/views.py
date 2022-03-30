from django.http import request
from django.shortcuts import render


# Create your views here.
def masterfn(request):
    return render(request,"master.html")
def homefn(request):
    return render(request,"home.html") 
# def aboutusfn(request):
#     return render(request,"aboutus.html")
def aboutusfn(request):
    return render(request,"aboutus.html") 
def fncontactus(request):
    return render(request,"contactus.html")
def carsfn(request):
    return render(request,"cars.html")
def rgstrfn(request):
    return render(request,"register.html")
def autcarfn(request):
    return render(request,"autcar.html")
def mancarfn(request):
     return render(request,"mancar.html")
def wedcarfn(request):
    return render(request,'wedcar.html')   
def bookregfn(request):
    return render(request,"bookreg.html")  
def fnshome(request):
    return render(request,"samplehome.html")
def fnbkcar(request):
    return render(request,"bookcar.html")

    

    