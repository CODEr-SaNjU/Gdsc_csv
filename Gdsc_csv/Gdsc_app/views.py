from django.shortcuts import render ,redirect 
from django.http import HttpResponse, Http404
import re
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage
from .models import Documents
import csv ,io , requests
from .forms import DocumentForm
from selenium import webdriver
from django.http import FileResponse


# Create your views here.

def Download_csv(request):
    pass
    # return render(request,'html_files/Download.htm')

def csv_files(request):
    if request.method == 'POST' and request.FILES['files']:
        myfile = request.FILES['files']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = os.path.join(settings.BASE_DIR+fs.url(filename))
        if os.path.exists(uploaded_file_url)==True:
            with open(uploaded_file_url,'r') as csvfile:
                csvfile = csvfile.readlines()
                for csvline in csvfile:
                    if csvline == '\n':
                        continue
                    csvline = re.sub(',,+','',csvline)
                    csvlinelist = csvline.split(',')
                    if len(csvlinelist) == 1:
                        uploaded_file_url_1 = os.path.join(settings.MEDIA_ROOT,csvline.strip('\n')+'.csv')
                        print(uploaded_file_url_1)
                        subcsvfile=open(uploaded_file_url_1,'w',)
                        continue
                    new_file_csv = subcsvfile.write(csvline)
                return HttpResponse(uploaded_file_url_1)
            return render(request, 'html_files/Home.htm',{"uploaded_file_url_1":uploaded_file_url_1})
        else:
            return HttpResponse("please remove space from filename ya add _ in filename")

    return render(request, 'html_files/Home.htm')




def download(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT, Path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.csv")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404