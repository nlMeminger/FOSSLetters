from django import forms
from letter.models import Letter
from django.forms import ModelForm

class PostForm(forms.ModelForm):
	class Meta:
		model = Letter
		fields = ['letter', 'cur_r', 'cur_g', 'cur_b']
		widgets = {
			'letter' : forms.TextInput(),
			'cur_r' : forms.TextInput(),
			'cur_g' : forms.TextInput(),
			'cur_b' : forms.TextInput(),
		}
