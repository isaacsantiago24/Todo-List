from django.contrib import admin

# Register your models here.

#import models
from .models import *

#Task is the name of the class inside models.py
admin.site.register(Task)