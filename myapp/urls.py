from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[ 
    path('',views.table ,name="table" ) ,
    path('index',views.index ,name="index") ,
    path('add' , views.add ,name="add") ,
    path('table',views.table ,name="table" ),
    path(r'^changestatus/(?P<id>\d+)/$', views.changestatus ,name="changestatus"),
    path(r'^update/(?P<id>\d+)/$' , views.update ,name="update"),
    path(r'^edit/(?P<id>\d+)/$' , views.edit ,name="edit"),
    path(r'^delete/(?P<id>\d+)/$' , views.delete ,name="delete"),
    path('search' , views.search ,name="search") ,
    path('search_page' , views.search_page ,name="search_page")
]