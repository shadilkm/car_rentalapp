from django.urls import path,include
from django.urls.resolvers import URLPattern
from . import views
urlpatterns=[
    path('masterpg',views.masterpgfn,name='masterpg'),
    path('dlhome',views.dashbdfn,name='dashboard'),
    path('dealers',views.dealersfn,name='dealers'),
    path('register',views.rgstrfn,name='dealerreg'),
    path('review',views.fnreview,name='review'),
    path('customer',views.fncust,name='customer'),
    path('reguser',views.fnreguser,name='reguser'),
    path('cars2',views.fncars2,name='cars2'),
    path('reports',views.fnpreports,name='reports'),
    path('feedback',views.fnfdback,name='feedback'),
    path('carvariant',views.fncvariant,name='carvariant'),
    path('addcarvariant',views.fnaddcvariant,name='addcarvariant'),
    path('category',views.fncategory,name='category')
    
]