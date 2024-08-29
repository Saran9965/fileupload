from django.shortcuts import render,redirect
from .forms import myfileForm
from .models import myfileupload
from django.contrib import messages
from django.urls import path
import os

def home(req):
    mydata=myfileupload.objects.all() # retrive all images in variable
    myform=myfileForm()
    if(mydata!=''):
        context={'form':myform,'mydata':mydata}
        return render(req,'index.html',context)
    else:
        context={'form':myform}
        return render(req,'index.html',context)

def uploadfile(req):
     if req.method=='POST':
        myform=myfileForm(req.POST,req.FILES)
        if myform.is_valid():
            filename=req.POST.get('file_name')
            files=req.FILES.get('file')
            
            exists=myfileupload.objects.filter(my_file=files).exists()  # if file is already uploaded to reject that
            if exists:
                messages.error(req,'The file %s is already exists...!!!'%files)
            else:
                myfileupload.objects.create(file_name=filename,my_file=files).save()
                messages.success(req,'File Upload successfull...')
        return redirect('home')
     
def deletefile(req,id):
    mydata=myfileupload.objects.get(id=id)
    mydata.delete()
    os.remove(mydata.my_file.path)
    messages.success(req,'File Delete sucessfully...')
    return redirect('home')
