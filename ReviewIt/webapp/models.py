from django.db import models

class ModelFormWithFileField(models.Model):
   name = models.CharField(max_length = 500)
   file = models.FileField(upload_to = 'media')
