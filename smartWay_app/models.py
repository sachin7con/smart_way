from django.db import models

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    clas = models.IntegerField(null=True)
    FeeSubmitDate = models.DateField(null=True)
    phone = models.IntegerField(null=True)
    joining_date = models.DateField(null=True)
    Fee = models.IntegerField(null=True)
