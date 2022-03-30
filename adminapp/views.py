from django.http import request
from django.shortcuts import render


# Create your views here.
def masterpgfn(request):
    return render(request,"master1.html")
def dashbdfn(request):
    return render(request,"dashboard.html")
def dealersfn(request):
    return render(request,"dealers.html")
def rgstrfn(request):
    return render(request,"regbook.html")
def fnreview(request):
    return render(request,"review.html")
def fncust (request):
    return render(request,"customer.html")
def fnreguser(request):
    return render(request,"reguser.html")
def fncars2 (request):
    return render(request,"cars2.html")
def fnpreports (request):
    return render (request,"reports.html")
def fnfdback (request):
    return render(request,"feedback.html")
def fncvariant (request):
    return render (request,"carvariant.html")
def fnaddcvariant(request):
    return render(request,"addcarvariant.html")
def fncategory (request):
    return render(request,"category.html")
