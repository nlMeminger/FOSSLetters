from django.shortcuts import render
from django.http import HttpResponse
from letter.models import Letter
from bfgmagicletters import opc
# from bfgmagicletters import color_utils
from .forms import PostForm
# import time
# import math
# import sys
# import logging
import json


def create_post(request):
	"""Create a post and updates the db."""
	if request.method == 'POST':
		letter_update = request.POST
		response_data = {}
		post = Letter.objects.get(letter=letter_update['letter'])
		post.cur_r = letter_update['cur_r']
		post.cur_g = letter_update['cur_g']
		post.cur_b = letter_update['cur_b']
		post.save()
		let = letter_update['letter']

		IP_PORT = '127.0.0.1:7890'
		client = opc.Client(IP_PORT)

		if let == "M":
			start_pixels = 0
			end_pixels = 46
			cur_channel = 0
		elif let == "A":
			start_pixels = 47
			end_pixels = 87
			cur_channel = 1
		elif let == "G":
			start_pixels = 88
			end_pixels = 128
			cur_channel = 2
		elif let == "I":
			start_pixels = 129
			end_pixels = 145
			cur_channel = 3
		else:
			start_pixels = 174
			end_pixels = 198
			cur_channel = 4


		fps = 60

		pixels = []
		# for ii in range(start_pixels, end_pixels):
		for ii in range(0, 900):
			# pct = (ii / n_pixels)
			r = post.cur_r
			g = post.cur_g
			b = post.cur_b
			pixels.append((r, g, b))
		client.put_pixels(pixels, channel=cur_channel)


		return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/json")


def create_reset(request):
	"""Create a reset color to default call"""
	if request.method == 'GET':
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
		response_data = {'success': 1}
	return HttpResponse(
		json.dumps(response_data), content_type="application/json")


def home(request):
	"""Load page"""
	letter_M = Letter.objects.get(letter='M')
	letter_A = Letter.objects.get(letter='A')
	letter_G = Letter.objects.get(letter='G')
	letter_I = Letter.objects.get(letter='I')
	letter_C = Letter.objects.get(letter='C')
	form = PostForm()

	IP_PORT = '127.0.0.1:7890'
	client = opc.Client(IP_PORT)

	n_pixels = 30
	fps = 60

	pixels = []
	for ii in range(n_pixels):
		pct = (ii / n_pixels)
		r = letter_A.cur_r
		g = letter_A.cur_g
		b = letter_A.cur_b
		pixels.append((r, g, b))
	client.put_pixels(pixels, channel=0)

	return render(request, 'letters.html', {
		'M': letter_M, 'A': letter_A, 'G': letter_G,
		'I': letter_I, 'C': letter_C, 'form': form})
