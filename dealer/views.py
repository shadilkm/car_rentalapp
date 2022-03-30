from django.http import request
from django.shortcuts import render

# Create your views here.



def dlmasterfn(request):
    return render(request,"dlmaster.html")
def dldashboardfn(request):
    return render(request,"dldashboard.html")
