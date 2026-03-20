from django.db import models

# Create your models here.

class LoginPage(models.Model):
	user = models.CharField(max_length=15)
	pwd = models.CharField(max_length=15)

	def __str__(self):
		return self.user

class RegisterPage(models.Model):
	fname = models.CharField(max_length=15)
	lname = models.CharField(max_length=15)
	mail = models.CharField(max_length=25)
	phone = models.CharField(max_length=10)
	user = models.CharField(max_length=15)
	pwd = models.CharField(max_length=15)

	def _str__(self):
		return self.mail+" "+self.user
