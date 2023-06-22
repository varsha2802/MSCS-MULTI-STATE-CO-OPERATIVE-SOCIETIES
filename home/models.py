from django.db import models

# Create your models here.
from django.db import models
from datetime import date

# Create your models here.
class Registration(models.Model):
   
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    
    mobile = models.IntegerField()
    email = models.EmailField(max_length=254)
    desig = models.CharField(max_length = 30)

    country = models.CharField(max_length = 30)
    state = models.CharField(max_length = 30)
    district = models.CharField(max_length = 30)

    md = models.CharField(max_length = 30)
    address = models.TextField()

    pan = models.IntegerField()
    tan = models.IntegerField()
    service = models.IntegerField()

    password = models.CharField(max_length = 30)
    confirm = models.CharField(max_length = 30)
    date=models.DateField()
       

    def __str__(self):
        return self.username
    


class GraphData(models.Model):
    name = models.CharField(max_length=255)
    graph_data = models.TextField()
    graph_img=models.ImageField(upload_to='None', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.name

class Grievance(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=254)
    typeofcomplaint=models.CharField(max_length=30)
    societycomplaint=models.CharField(max_length=150)
    complaint= models.TextField()
    date=models.DateField()


    def __str__(self):
        return self.fname
    
class Feedback(models.Model):
    typeoffeedback=models.CharField(max_length=50)
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=254)
    mobile = models.IntegerField()
    address = models.TextField()
    subject = models.TextField()
    file= models.FileField(upload_to="feedback/",null="True")
    date=models.DateField()


    def __str__(self):
        return self.name


    