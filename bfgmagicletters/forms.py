from django import forms
from letter.models import Letter

class PostForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = ['letter', 'cur_r', 'cur_g', 'cur_b']
        widgets = {
            'letter': forms.TextInput(attrs={
                id='letter-text'
            }),
            'cur_r': forms.TextInput(attrs={
                id='r-text'
            }),
            'cur_g': forms.TextInput(attrs={
                id='g-text'
            }),
            'cur_b': forms.TextInput(attrs={
                id='b-text'
            }),
        }
