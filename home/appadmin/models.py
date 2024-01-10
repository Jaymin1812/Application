from django.db import models

from django.utils import timezone

from datetime import datetime

# from PIL import Image

class Detail(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    dob=models.DateField()
    age=models.CharField(max_length=3)
    gender=models.CharField(max_length=20,choices=(('male','male'),('female','female')))
    missing_date=models.DateTimeField()
    city=models.CharField(max_length=70)
    status=models.CharField(max_length=20,choices=(('Active','Active'),('Inactive','Inactive')),default='Active')
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='filepath/',null=True,blank=True)