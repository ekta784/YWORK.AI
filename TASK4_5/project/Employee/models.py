from django.db import models
import uuid


# Create your models here.
class Deptable(models.Model):
    id= models.UUID(primary_key=True, default=uuid.uuid4, editable=False)
    name= models.CharField(max_length=20) 


def __str__(self):
    return self.name    


class Emptable(models.Model):
    id= models.IntegerField(primary_key=True)
    name= models.CharField(max_length=20) 
    baseSalary= models.IntegerField()
    departmentId= models.ForeignKey(Deptable, on_delete=models.CASCADE)

def __str__(self):
    return self.name

