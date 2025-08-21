from django.db import models


# Create your models here.

class Emptable(models.Model):
    id= models.IntegerField(primary_key=id)
    name= models.CharField(max_length=20) 
    baseSalary= models.IntegerField()
    departmentId= models.IntegerField()

def __str__(self):
    return self.name

