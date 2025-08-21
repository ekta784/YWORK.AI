from django.db import models

class Emptable(models.Model):
     id= models.IntegerField(primary_key=True)
     name= models.CharField(max_length=20)
     baseSalary= models.IntegerField() 
     departmentId= models.IntegerField()

def __str__(self):
       return self.name

class Deptable(models.Model): 
    id= models.IntegerField(primary_key=True) 
    name= models.CharField(max_length=20)

def __str__(self):
       return self.name