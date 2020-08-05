from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add a new task'}))

    class Meta:
        #which model do we want to create a form? Task.
        model = Task
        fields = '__all__'