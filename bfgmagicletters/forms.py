from django import forms

class ColorForm(forms.Form):
    colorChange = forms.CharField(label='Color Hex', max_length=6)