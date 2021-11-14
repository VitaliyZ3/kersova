
from django import forms
from .models import *

class AddTreanerForm(forms.ModelForm):

    class Meta:
        model = Trainer
        fields = ['name', 'surname','about', 'photo', 'price']
        exclude = ['name', 'surname']        
