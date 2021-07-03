from catalogo.models import book, Author
from django import forms
from django.forms.models import ModelForm

#Formulario genérico
class bookform(forms.Form):
    title = forms.CharField(label='titulo')
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    editorial = forms.CharField(label='editorial')
    year = forms.IntegerField(label='year')
    volumen = forms.FileField(label='volumen')

#Formulario de Modelo    
class modelbookform(ModelForm):
    class Meta:
        model = book
        fields = ['title','author','editorial','year','volumen'] #Eliminar author

