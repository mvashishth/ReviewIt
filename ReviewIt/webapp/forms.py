from django import forms
import random
import os
from .opencv_processing import extractFrames

class UploadFileForm(forms.Form):
	file = forms.FileField()




def handle_uploaded_file(f):
	while 1>0:
		

		directory_existence_check=os.path.isdir('/media/mayur/2ef007f3-505d-4f8d-98f8-efe8bfc991c5/ReviewIt/ReviewIt/webapp/media/user')
		path_name='/media/mayur/2ef007f3-505d-4f8d-98f8-efe8bfc991c5/ReviewIt/ReviewIt/webapp/media/user'
		if directory_existence_check==False:
			os.mkdir(path_name)
			break
			


	with open(path_name+'/'+'video','wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
	extractFrames(path_name+'/'+'video', path_name+'/frame_data')
	dest=path_name+'/destination_data'
	os.mkdir(dest)
	z=[path_name,dest]
	return[path_name,dest]

