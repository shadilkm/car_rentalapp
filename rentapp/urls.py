from django.urls import path,include
from django.urls.resolvers import URLPattern
from . import views
urlpatterns=[
    path('masterpage',views.masterfn,name='master'),
    path('home',views.homefn,name='home'),
    path('aboutus',views.aboutusfn,name='aboutus'),
    path('contactus',views.fncontactus,name='contactus'),
    # path('',views.aboutusfn,name='aboutus'),
    path('cars',views.carsfn,name='cars'),
    path('register',views.rgstrfn,name='register'),
    path('autcar',views.autcarfn,name='automaticcar'),
    path('mancar',views.mancarfn,name='manualcar'),
    path('wedcar',views.wedcarfn,name='weddingcar'),
    path('bookreg',views.bookregfn,name='bookreg'),
    path('shome',views.fnshome,name='shome'),
    path('bkcar',views.fnbkcar,name='bookcar')
    
]