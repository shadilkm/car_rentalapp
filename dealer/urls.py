from django.urls import path,include
from django.urls.resolvers import URLPattern
from . import views
urlpatterns=[
        path('dlmaster',views.dlmasterfn,name='dealermaster'),
        path('dldashboard2',views.dldashboardfn,name='dldashboard')

    
]