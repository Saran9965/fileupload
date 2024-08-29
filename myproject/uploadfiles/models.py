from django.db import models

# Create your models here.
class myfileupload(models.Model):
    file_name=models.CharField(max_length=20)
    my_file=models.FileField()