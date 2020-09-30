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
    return render(request,'html_files/Home.htm')

def csv_files(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'html_files/Home.htm')
    else:
        form = DocumentForm()
    return render(request,'html_files/Home.htm',{'form':form})
        


