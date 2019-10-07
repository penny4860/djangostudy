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
    ff = open("tmp.txt", 'r')
    data = ff.read()
    ff.close()
    return data

def upload_file(request):
    if request.method == 'POST':
        # print("upload_file(request):=========================================")
        # print(request.FILES)
        # print(request.FILES['file'])
        # print("==============================================================")
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            contents = handle_uploaded_file(request.FILES['file'])
            # print(contents)
            # return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
        contents = "Nothing"
    return render(request, 'upload.html', {'form': form, "contents": contents})