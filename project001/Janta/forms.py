from dataclasses import fields
from django.forms import ModelForm
from django import forms
from .models import *

class AddManagerForm(ModelForm):
    class Meta():
        model = Manager
        fields = '__all__'

class AddWriterForm(ModelForm):
    class Meta():
        model = Writer
        fields = '__all__'

class AddOrderForm(ModelForm):
    class Meta():
        model = Order
        fields = '__all__'
        # fields = ['writer','order_id']
        # # label = {
        # #     'writer':'Writer Name'
        # # }
        # widgets = {
        #     'writer': forms.Select(attrs={'class': 'form-control'}),
        #     'order_id': forms.TextInput(attrs={'class': 'form-control','id':'inlineFormInputName2MD', 'placeholder':'Jane Doe'}),
        # }
