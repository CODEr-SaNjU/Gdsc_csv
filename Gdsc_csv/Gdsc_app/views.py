from django.shortcuts import render ,redirect 
from django.http import HttpResponse
import re
from django.conf import settings
import os
# Create your views here.

def Home(request):
    return render(request,'html_files/Home.htm')

def csv_files(request):
    if request.method == 'POST':
        files = request.FILES['files']
        path_for_csv_file = os.path.join(settings.BASE_DIR)+f"/{files}"
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