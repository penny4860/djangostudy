from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from .forms import UploadFileForm

# from somewhere import handle_uploaded_file

# Imaginary function to handle an uploaded file.
def handle_uploaded_file(f):
    with open('tmp.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        
        print("upload_file(request):=========================================")
        print(request.FILES['title'])
        print(request.FILES['file'])
        print("==============================================================")
        
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})