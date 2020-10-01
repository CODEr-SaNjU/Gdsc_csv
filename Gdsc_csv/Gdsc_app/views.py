from django.shortcuts import render ,redirect 
from django.http import HttpResponse
import re
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage
from .models import Documents
import csv ,io
from .forms import DocumentForm
# Create your views here.

def Download_csv(request):
    return render(request,'html_files/Download.htm')

def csv_files(request):
    if request.method == 'POST' and request.FILES['files']:
        myfile = request.FILES['files']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = os.path.join(settings.BASE_DIR+fs.url(filename))
        with open(uploaded_file_url,'r') as csvfile:
            csvfile = csvfile.readlines()
            print(csvfile)
            for csvline in csvfile:
                if csvline == '\n':
                    continue
                csvline = re.sub(',,+','',csvline)
                csvlinelist = csvline.split(',')
                if len(csvlinelist) == 1:
                    subcsvfile = open(csvline.strip('\n')+'.csv','w')
        return render(request, 'html_files/Home.htm', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'html_files/Home.htm')



















    # if request.method == 'POST':
    #     form = DocumentForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return render(request,'html_files/Home.htm')
    # else:
    #     form = DocumentForm()
    # return render(request,'html_files/Home.htm',{'form':form})
        


