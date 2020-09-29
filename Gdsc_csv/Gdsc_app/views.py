from django.shortcuts import render ,redirect 
from django.http import HttpResponse
import re
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage
from .models import Documents
import csv ,io
# Create your views here.

def Home(request):
    return render(request,'html_files/Home.htm')

def csv_files(request):
    if request.method == 'POST' and request.FILES['files']:
        myfile = request.FILES['files']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        with open(uploaded_file_url,'r') as csvfile:
            for csvline in csvfile:
                if csvline == '\n':
                    continue
                csvline = re.sub(',,+','',csvline)
                csvlinelist = csvline.split(',')
                if len(csvlinelist) == 1:
                    subcsvfile = open(csvline.strip('\n')+'.csv','w')
                    continue
        return render(request,'html_files/Home.htm', {
            'uploaded_file_url': subcsvfile
        })
    return redirect('Home')