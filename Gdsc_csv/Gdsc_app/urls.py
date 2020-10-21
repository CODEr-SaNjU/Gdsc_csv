from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('csv_file',views.csv_files,name="csv_file"),
    path('',views.index,name="index")


]