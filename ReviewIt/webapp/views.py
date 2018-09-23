from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm

from .forms import handle_uploaded_file



def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
    
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse('ThankYou')
    else:
        form = UploadFileForm()
    return render(request, 'home.html', {'form': form})