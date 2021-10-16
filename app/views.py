from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.core.files.storage import FileSystemStorage
# Create your views here.


def upload(request):

    if request.method == 'POST':
            myfile = request.FILES['file'] # this is my file
            print(myfile)
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return HttpResponse("File Uploaded.")
    else:
        return render(request, 'globalpage.html')
