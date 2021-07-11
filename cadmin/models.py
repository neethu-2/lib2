from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
class bookstb(models.Model):
	Title=models.CharField(max_length=30,default='')
	
	Bookstock=models.PositiveIntegerField()
	Author=models.CharField(max_length=30,default='')
	Publications=models.CharField(max_length=30,default='')
	Price=models.PositiveIntegerField()
	Edition=models.CharField(max_length=30,default='')

	Dateofpublications=models.DateField()
	Photo = models.FileField(default='')
	def __str__(self):
		return self.Title