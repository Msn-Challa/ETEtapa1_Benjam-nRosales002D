from django import forms
from django.forms import ModelForm, fields, widgets
from .models import Proveedor

class ProveedorForm(ModelForm):
    class Meta:
        model= Proveedor
        fields=['idProv', 'img', 'nombreP', 'numTf', 'dire', 'email', 'pais', 'moneda', 'categoria']
        labels = {
            'idProv':'Ingrese número de identificación',
            'img':'Ingrese logo de proveedor',
            'nombreP':'Ingrese nombre de proveedor',
            'numTf':'Ingrese número de proveedor',
            'dire':'Ingrese dirección de proveedor',
            'email':'Ingrese email de proveedor',
            'pais':'Ingrese País de proveedor',
            'moneda':'Especifique moneda de pago (Pesos o dólares)',
            'categoria':'Seleccione categoria del proveedor'
        }
        widgets={
            'idProv': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Número de identificación',
                    'id':'idProv'
                }
            ),
            'img': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id':'img'
                }
            ),
            'nombreP': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nombre de proveedor',
                    'id':'nombreP'
                }
            ),
            'numTf': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Número de proveedor',
                    'id':'numTf'
                }
            ),
            'dire': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Dirección de proveedor',
                    'id':'dire'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Email de proveedor',
                    'id':'email'
                }
            ),
            'pais': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'País de proveedor',
                    'id':'pais'
                }
            ),
            'moneda': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Moneda de pago',
                    'id':'moneda'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'categoria'
                }
            )
        }