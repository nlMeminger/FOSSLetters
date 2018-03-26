from django.shortcuts import render
from letter.models import Letter

def home(request):
	letter_M = Letter.objects.get(letter='M')
	return render(request, 'letters.html', {'letter': letter_M})
