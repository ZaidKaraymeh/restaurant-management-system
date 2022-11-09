from django import forms
from .models import *

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'
        exclude = ['restaurant']

        widgets = {
            'name': forms.TextInput(),
            'price': forms.TextInput(),
            'caption': forms.TextInput(),
            'description': forms.Textarea(),
        }
    
    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['style'] = 'height:50px;'
        self.fields['price'].widget.attrs['style'] = 'height:50px;'
        self.fields['caption'].widget.attrs['style'] = 'height:50px;'
        self.fields['description'].widget.attrs['style'] = 'height:50px;'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['caption'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'

class FoodTypeForm(forms.ModelForm):
    class Meta:
        model = FoodType
        fields = '__all__'
        exclude = ['restaurant']

        widgets = {
            'type': forms.Select(),
        }
    
    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)

        self.fields['type'].widget.attrs['style'] = 'height:50px;'
        self.fields['type'].widget.attrs['class'] = 'form-select'


class FoodCartForm(forms.ModelForm):
    class Meta:
        model = FoodCart
        fields = '__all__'
        exclude = ['restaurant', 'food']

        widgets = {
            'description': forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)

        self.fields['description'].widget.attrs['style'] = 'height:50px;'
        self.fields['description'].widget.attrs['class'] = 'form-control'
