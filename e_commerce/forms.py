from unicodedata import name
from django.forms import ModelForm
from .models import Product
from django import forms


class AddProductForm(ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    price = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'number'}))
    stock = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'number'}))
    imageUrl = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        self.fields['stock'].widget.attrs['min'] = 1

    class Meta:
        model = Product
        fields = '__all__'



class UpdateProductForm(ModelForm):
    id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly':'true','maxlength':'10'}))
    name = forms.CharField(max_length = 30 , widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Name"}))
    description = forms.CharField(max_length = 30 , widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Description"}))
    price = forms.FloatField( widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Price'}))
    stock = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Stock'}))
    imageUrl = forms.CharField(max_length = 2500 , widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"ImageUrl" }))

    def __init__(self, *args, **kwargs):
        super(UpdateProductForm, self).__init__(*args, **kwargs)
        self.fields['stock'].widget.attrs['min'] = 1
        self.fields['price'].widget.attrs['min'] = 1

    class Meta():
        model = Product
        fields = '__all__'