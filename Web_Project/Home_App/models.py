from django.db import models
from django.contrib.auth.models import User

    


# Create your models here.

class EventCategory(models.Model):
    name=models.CharField(null=True, max_length=200)

    def __str__(self):
        return self.name

class Event(models.Model):
    image=models.ImageField(upload_to='static',blank=True,null=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    date=models.DateField()
    category=models.ManyToManyField(EventCategory)

    def __str__(self):
        return self.title

class Contact_Us (models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    subject=models.TextField(null=True)
    message=models.TextField(null=True)
    date=models.DateField()

    def __str__(self):
        return self.name

class Student(models.Model):
    user=models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name=models.CharField(null=True, max_length=200)
    phone=models.CharField(null=True, max_length=200)
    email=models.CharField(null=True, max_length=200)
    profile_pic=models.ImageField(default='static/images/profile_pic.profile_pic.jpg',upload_to='static/images',blank=True,null=True)
    date_created=models.DateField(null=True, auto_now_add=True)
    
    def __str__(self):
        return self.name

class User_Registration(models.Model):
    name=models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    event_name=models.ForeignKey(Event, null=True, on_delete=models.CASCADE)
    course=models.CharField(max_length=100)
    semester=models.IntegerField()
    mobile_no=models.CharField(max_length=15, blank=True,null=True)
    email=models.CharField(max_length=122)
    date=models.DateField()
    
    def __str__(self):
        return self.name.name
    



       
    
    

  



   
    
    
    
    




