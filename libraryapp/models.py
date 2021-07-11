from django.db import models
from django.core.validators import RegexValidator
from datetime import date

class regtable(models.Model):
	Name=models.CharField(max_length=30,default='')
	Gender=models.CharField(max_length=30,default='')
	Address=models.CharField(max_length=30,default='')
	Mobile=models.CharField(max_length=10,blank=True)
	Email=models.CharField(max_length=30,default='')
	Branch=models.CharField(max_length=30,default='')
	Semester=models.CharField(max_length=30,default='')
	Regno=models.CharField(max_length=30,default='')
	Place=models.CharField(max_length=30,default='')
	Username=models.CharField(max_length=30,default='')
	Password=models.CharField(max_length=30,default='')
	Photo = models.FileField(default='')
	def __str__(self):
		return self.Name


# Create your models here.
class chtable(models.Model):
	
	Studentname=models.CharField(max_length=30,default='')
	
	# Regtable=models.ForeignKey(regtable,on_delete=models.CASCADE)
	
	Booktitle=models.CharField(max_length=30,default='')
	
	Author=models.CharField(max_length=30,default='')
	Date=models.DateField(max_length=30)
	
	def __str__(self):
		return self.Studentname

class returnbooktb(models.Model):
	# Studentname=models.CharField(max_length=30,default='')
	Regno=models.CharField(max_length=30,default='')
	Booktitle=models.CharField(max_length=30,default='')
	
	Author=models.CharField(max_length=30,default='')
	Returnstatus=models.CharField(max_length=30,default='')
	Duedate=models.DateField(max_length=30)
	Returndate=models.DateField(max_length=30)
	def __str__(self):
		return self.Regno
class fbtb(models.Model):
	
	Name=models.CharField(max_length=30,default='')
	Email=models.CharField(max_length=30,default='')
	Feedback=models.CharField(max_length=30,default='')
	
	def __str__(self):
		return self.Name

class issuebtb(models.Model):
	Name=models.CharField(max_length=30,default='')
	Regno=models.CharField(max_length=30,default='')
	Booktitle=models.CharField(max_length=30,default='')
	Edition=models.CharField(max_length=30,default='')
	Author=models.CharField(max_length=30,default='')
	Publications=models.CharField(max_length=30,default='')
	Date=models.DateField(null=False)
	Mobile=models.CharField(max_length=30,default='')
	
	Photo = models.FileField(default='')
	def __str__(self):
		return self.Name

class Finetb(models.Model):
	Name=models.CharField(max_length=30,default='')
	Branch=models.CharField(max_length=30,default='')
	Amount=models.PositiveIntegerField()
	Date=models.DateField(max_length=30)