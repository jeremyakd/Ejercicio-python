from django.db.models.fields import TextField
from .models import Coche, Camioneta, Bicicleta, Motocicleta
from django import forms



class CocheForm(forms.ModelForm):

    class Meta:
        model = Coche
        fields = ['color', 'ruedas', 'velocidad', 'cilindrada']
        widgets = {
            'color': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Color'}),
            'ruedas': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Ruedas'}),
            'velocidad': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Velocidad'}),
            'cilindrada': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Cilindrada'}),
        }
        labels = {
            'color':'', 'ruedas':'', 'velocidad':  '', 'cilindrada': ''
        }


class CamionetaForm(forms.ModelForm):

    class Meta:
        model = Camioneta
        fields = ['color', 'ruedas', 'velocidad', 'cilindrada', 'carga']
        widgets = {
            'color': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Color'}),
            'ruedas': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Ruedas'}),
            'velocidad': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Velocidad'}),
            'cilindrada': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Cilindrada'}),
            'carga': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Carga'}),
        }
        labels = {
            'color':'', 'ruedas':'', 'velocidad':  '', 'cilindrada': '', 'carga': '',
        }


class BicicletaForm(forms.ModelForm):

    class Meta:
        model = Bicicleta
        fields = ['color', 'ruedas', 'tipo']
        widgets = {
            'color': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Color'}),
            'ruedas': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Ruedas'}),
            'tipo': forms.Select(attrs={'class':'form-select mt-3', 'placeholder':'tipo'}),
        }
        labels = {
            'color':'', 'ruedas':'', 'tipo':  '',
        }


class MotocicletaForm(forms.ModelForm):

    class Meta:
        model = Motocicleta
        fields = ['color', 'ruedas', 'tipo', 'velocidad', 'cilindrada']
        widgets = {
            'color': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Color'}),
            'ruedas': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Ruedas'}),
            'tipo': forms.Select(attrs={'class':'form-select mt-3', 'placeholder':'tipo'}),
            'velocidad': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Velocidad'}),
            'cilindrada': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Cilindrada'}),
        }
        labels = {
            'color':'', 'ruedas':'', 'cilindrada':  '', 'tipo':  '','velocidad':  '',
        }
