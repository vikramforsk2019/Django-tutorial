from django.db import models
import os
# Create your models here.
class User(models.Model):
    uname= models.CharField(max_length=30, unique=True)
    email= models.EmailField()
    file=  models.FileField() # for creating file input 

class Signup(models.Model):
	fname=models.CharField(max_length=30)
	lname=models.CharField(max_length=30)
	gender=models.CharField(max_length=30)
	email=models.CharField(max_length=30,unique=True)
	password=models.CharField(max_length=30)
	image=models.FileField()
	class Meta:
		db_table="signup"
