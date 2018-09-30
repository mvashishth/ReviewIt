from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
import random
from .forms import *
import sys
sys.path.append('/media/mayur/2ef007f3-505d-4f8d-98f8-efe8bfc991c5/ReviewIt/ReviewIt/webapp/dl_models/pytorch-yolo-v3')
from detection import * 

	
def upload_file(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
	
		if form.is_valid():
			print('Hello')
			handle_uploaded_file(request.FILES['file'])
			#return HttpResponse('ThankYou')
			return render(request, 'home.html', {'form': form})
	else:
		form = UploadFileForm()
	return render(request, 'home.html', {'form': form})




def yolo(request):
	output_evaluation()
	return HttpResponse('FuckThat')
