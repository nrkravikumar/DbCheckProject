from django.contrib import admin
from SampleApp . models import *

# Register your models here.

class LoginPageM(admin.ModelAdmin):
	d = ("user","pwd")

class RegisterPageM(admin.ModelAdmin):
	f = ("fname","lname","mail","phone","user","pwd")

admin.site.register(LoginPage,LoginPageM)
admin.site.register(RegisterPage,RegisterPageM)