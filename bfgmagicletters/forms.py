from django import forms
from letter.models import Letter

class PostForm(forms.ModelForm):
    name = forms.CharField(lable='Letter')
    cur_r = forms.TextInput()
    cur_g = forms.TextInput()
    cur_b = forms.TextInput()

    f=PostForm(auto_id=False)

    #class Meta:
    #    model = Letter
    #    fields = ['letter', 'cur_r', 'cur_g', 'cur_b']
    #    widgets = {
    #        'letter': forms.TextInput(attrs={'id': 'letter_input'}),
    #        'cur_r': forms.TextInput(),
    #        'cur_g': forms.TextInput(),
    #        'cur_b': forms.TextInput(),
    #    }
