
from django import forms
from .models import Userip

class Dgbbip(forms.ModelForm):
    class Meta:
        model = Userip
        fields= ['dia', 'rpm', 'rload', 'aload', 'lfactor', 'elife']
        labels = {
            'dia': ('Diameter d (mm)'),
        }
        widgets= {
            'dia': forms.NumberInput(attrs={'class': 'form-control'}),
            'rpm': forms.NumberInput(attrs={'class': 'form-control'}),
            'rload': forms.NumberInput(attrs={'class': 'form-control'}),
            'aload': forms.NumberInput(attrs={'class': 'form-control'}),
            'lfactor': forms.NumberInput(attrs={'class': 'form-control'}),
            'elife': forms.NumberInput(attrs={'class': 'form-control'}),
        }