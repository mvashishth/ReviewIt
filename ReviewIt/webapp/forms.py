from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=500)
    file = forms.FileField()


def handle_uploaded_file(f):
    with open('/media/mayur/2ef007f3-505d-4f8d-98f8-efe8bfc991c5/ReviewIt/ReviewIt/webapp/media') as destination:
        for chunk in f.chunks():
            destination.write(chunk)