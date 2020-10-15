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
from django.utils.encoding import smart_str
from wsgiref.util import FileWrapper



# Create your views here.
def Download_csv(request):
    pass
    # return render(request,'html_files/Download.htm')

def csv_files(request):
    if request.method == 'POST' and request.FILES['files']:
        myfile = request.FILES['files']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        print(filename)
        uploaded_file_url = os.path.join(settings.BASE_DIR+fs.url(filename))
        i = 0
        if os.path.exists(uploaded_file_url)==True:
            with open(uploaded_file_url,'r') as csvfile:
                csvfile = csvfile.readlines()
                new_File = "New_file_"+str(i)+".csv"
                os.rename(uploaded_file_url,new_File)
                print(new_File)
            if os.path.exists(new_File):
                with open(new_File, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type="text/csv;charset=utf-8;")
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(new_File)
                    return response
            raise Http404
            return render(request, 'html_files/Home.htm',)
        else:
            return HttpResponse("please remove space from filename ya add _ in filename")

    return render(request, 'html_files/Home.htm')







def download(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT, Path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="text/csv;charset=utf-8;")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404







#  for csvline in csvfile:
#                     if csvline == '\n':
#                         continue
#                     csvline = re.sub(',,+','',csvline)
#                     csvlinelist = csvline.split(',')
#                     if len(csvlinelist) == 1:
#                         print("len == 1")
#                         files_name=csvline.strip('\n')+'.csv'
#                         print("filename == ",files_name)
#                         uploaded_file_url_1 = os.path.join(settings.MEDIA_ROOT,files_name)
#                         subcsvfile=open(uploaded_file_url_1,'w',)
#                         continue
#                     new_file_csv = subcsvfile.write(csvline)
#                     print("last file data",new_file_csv)
#                 file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file_url_1)
#                 if os.path.exists(file_path):
#                     # subcsvfile_1 = open(file_path, 'w')
#                     with open(file_path, 'w') as fh:
#                         response = HttpResponse(new_file_csv, content_type="text/csv;charset=utf-8;")
#                         response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
#                         return response
#                 raise Http404
