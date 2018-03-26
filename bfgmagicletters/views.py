from django.shortcuts import render
from letter.models import Letter

def home(request):
	letter_M = Letter.objects.get(letter='M')
	letter_A = Letter.objects.get(letter='A')
	letter_G = Letter.objects.get(letter='G')
	letter_I = Letter.objects.get(letter='I')
	letter_C = Letter.objects.get(letter='C')
	return render(request, 'letters.html', {'M': letter_M, 'A': letter_A, 'G': letter_G, 'I': letter_I, 'C': letter_C})
