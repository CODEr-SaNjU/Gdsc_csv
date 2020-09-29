from django.shortcuts import render ,redirect 
from django.http import HttpResponse
import re
from django.conf import settings
import os
import csv ,io
# Create your views here.

def Home(request):
    return render(request,'html_files/Home.htm')

def csv_files(request):
    if "POST" == request.method:
        files = request.FILES['files']
        path_for_csv_file = (f"../../../{files}")
        print(path_for_csv_file)
        with open(path_for_csv_file,'r') as csvfile:
            for csvline in csvfile:
                if csvline == '\n':
                    continue
                csvline = re.sub(',,+','',csvline)
                csvlinelist = csvline.split(',')
                if len(csvlinelist) == 1:
                    subcsvfile = open(csvline.strip('\n')+'.csv','w')
                    continue
    return HttpResponse('csv created successfully')