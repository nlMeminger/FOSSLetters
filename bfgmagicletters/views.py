from django.shortcuts import render
from django.http import HttpResponse
from letter.models import Letter
from bfgmagicletters import opc
from bfgmagicletters import color_utils
from .forms import PostForm
import time
import math
import sys
import logging
import json

def create_post(request):
	if request.method == 'POST':
		letter_update = request.POST
		response_data = {}
		post = Letter.objects.get(letter=letter_update['letter'])
		post.cur_r = letter_update['cur_r']
		post.cur_g = letter_update['cur_g']
		post.cur_b = letter_update['cur_b']
		post.save()

		response_data['result'] = 'Create post successful!'
		response_data['letter'] = post.letter
		response_data['cur_r'] = post.cur_r
		response_data['cur_g'] = post.cur_g
		response_data['cur_b'] = post.cur_b

		return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")

def create_reset(request):
	if request.method == 'POST':
		response_data = {}
		post = Letter.objects.get(letter='M')
		post.cur_r = post.def_r
		post.cur_g = post.def_g
		post.cur_b = post.def_b

		post.save()

		post = Letter.objects.get(letter='A')
		post.cur_r = post.def_r
		post.cur_g = post.def_g
		post.cur_b = post.def_b

		post.save()

		post = Letter.objects.get(letter='G')
		post.cur_r = post.def_r
		post.cur_g = post.def_g
		post.cur_b = post.def_b

		post.save()

		post = Letter.objects.get(letter='I')
		post.cur_r = post.def_r
		post.cur_g = post.def_g
		post.cur_b = post.def_b

		post.save()

		post = Letter.objects.get(letter='C')
		post.cur_r = post.def_r
		post.cur_g = post.def_g
		post.cur_b = post.def_b

		post.save()
	return HttpResponse(content_type="application/json")
	#return render(request, 'letters.html',  {'M': letter_M, 'A': letter_A, 'G': letter_G, 'I': letter_I, 'C': letter_C})


def home(request):
	letter_M = Letter.objects.get(letter='M')
	letter_A = Letter.objects.get(letter='A')
	letter_G = Letter.objects.get(letter='G')
	letter_I = Letter.objects.get(letter='I')
	letter_C = Letter.objects.get(letter='C')
	form = PostForm()

	IP_PORT = '127.0.0.1:7890'
	client = opc.Client(IP_PORT)

	n_pixels = 20
	fps = 60

	pixels = []
	for ii in range(n_pixels):
		pct = (ii / n_pixels)
		r = 255
		g = 0
		b = 0
		pixels.append((r, g, b))
	client.put_pixels(pixels, channel=0)

	return render(request, 'letters.html', {'M': letter_M, 'A': letter_A, 'G': letter_G, 'I': letter_I, 'C': letter_C, 'form': form})
