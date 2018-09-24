from django import forms
import random
import os

from .opencv_processing import extractFrames
class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length=500)
    file = forms.FileField()



def handle_uploaded_file(f):
	while 1>0:
		file_end=random.randint(1,10000000)

		directory_existence_check=os.path.isdir('/media/mayur/2ef007f3-505d-4f8d-98f8-efe8bfc991c5/ReviewIt/ReviewIt/webapp/media/'+str(file_end))
		path_name='/media/mayur/2ef007f3-505d-4f8d-98f8-efe8bfc991c5/ReviewIt/ReviewIt/webapp/media/'+str(file_end)
		if directory_existence_check==False:
			os.mkdir(path_name)
			break

	with open(path_name+'/'+str(file_end),'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
	extractFrames(path_name+'/'+str(file_end), path_name+'/frame_data')