from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.Home,name='Home'),
    path('csv_files/',views.csv_files,name="csv_file")

]