from django.db import models

# Create your models here.
class student(models.Model):
    Rollno=models.IntegerField()
    Name=models.CharField(max_length=40)
    Email=models.EmailField()
    PhoneNo=models.IntegerField()
    