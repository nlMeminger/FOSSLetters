from django import forms
from letter.models import Letter


class PostForm(forms.ModelForm):
	"""Recieves the data from the form."""

	class Meta:
		"""Inserts the form data."""

		model = Letter
		fields = ['letter', 'cur_r', 'cur_g', 'cur_b']
		widgets = {
			'letter': forms.TextInput(),
			'cur_r': forms.TextInput(),
			'cur_g': forms.TextInput(),
			'cur_b': forms.TextInput(),
		}
