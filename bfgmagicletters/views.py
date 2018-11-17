from django.shortcuts import render
from django.http import HttpResponse
from letter.models import Letter
from bfgmagicletters import opc
from twilio.twiml.messaging_response import MessagingResponse
import webcolors, re
# from bfgmagicletters import color_utils
from .forms import PostForm
# import time
# import math
# import sys
# import logging
import json

def sms_push(request):
    ## 1 Get letter
    inp_str = request.POST["Body"]
    inp_str = inp_str.replace(' ', '')
    if any(i in inp_str[0].upper() for i in letters):
        let = inp_str[0].upper()
        color_str = inp_str[1:]
        ## 2 Get RGB if it exists
        if(re.match(rgb, color_str)):
            if all(0 <= int(group) <= 255 for group in re.match(rgb, color_str).groups()):
                color = re.match(rgb,color_str).groups()
                cur_r = color[0]
                cur_g = color[1]
                cur_b = color[2]
                print('rgb')
        ## 3 Get Hex if exists
        elif re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color_str):
            color = webcolors.hex_to_rgb(color_str)
            cur_r = color.red
            cur_g = color.green
            cur_b = color.blue
            print('hex')
        # 4 Get color from CSS3 name if it exists
        elif color_str in webcolors.CSS3_NAMES_TO_HEX:
            color = webcolors.name_to_rgb(color_str)
            cur_r = color.red
            cur_g = color.green
            cur_b = color.blue
            print('name')
    post_data = [('method', 'POST'),('letter','M'),('cur_r','255'),('cur_g', '0'),('cur_b', '0')]     # a sequence of two element tuples
    req = requests.porst()
    req.method = "POST"


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
                    cur_channel = 0
                elif let == "A":
                    cur_channel = 1
                elif let == "G":
                    cur_channel = 2
                elif let == "I":
                    cur_channel = 3
                else:
                    cur_channel = 4

                fps = 60

                pixels = []
                for ii in range(0, 900):
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
		pixels = []
		IP_PORT = '127.0.0.1:7890'
		client = opc.Client(IP_PORT)

		post = Letter.objects.get(letter='M')
		post.cur_r = post.def_r
		post.cur_g = post.def_g
		post.cur_b = post.def_b
		post.save()
		for ii in range(0, 512):
			r = post.cur_r
			g = post.cur_g
			b = post.cur_b
			pixels.append((r, g, b))
		client.put_pixels(pixels, channel=0)

		pixels = []
		post = Letter.objects.get(letter='A')
		post.cur_r = post.def_r
		post.cur_g = post.def_g
		post.cur_b = post.def_b
		post.save()
		for ii in range(0, 512):
			# pct = (ii / n_pixels)
			r = post.cur_r
			g = post.cur_g
			b = post.cur_b
			pixels.append((r, g, b))
		client.put_pixels(pixels, channel=1)

		pixels = []
		post = Letter.objects.get(letter='G')
		post.cur_r = post.def_r
		post.cur_g = post.def_g
		post.cur_b = post.def_b
		post.save()
		for ii in range(0, 512):
			r = post.cur_r
			g = post.cur_g
			b = post.cur_b
			pixels.append((r, g, b))
		client.put_pixels(pixels, channel=2)

		pixels = []
		post = Letter.objects.get(letter='I')
		post.cur_r = post.def_r
		post.cur_g = post.def_g
		post.cur_b = post.def_b
		post.save()
		for ii in range(0, 512):
			r = post.cur_r
			g = post.cur_g
			b = post.cur_b
			pixels.append((r, g, b))
		client.put_pixels(pixels, channel=3)

		pixels = []
		post = Letter.objects.get(letter='C')
		post.cur_r = post.def_r
		post.cur_g = post.def_g
		post.cur_b = post.def_b
		post.save()
		for ii in range(0, 512):
			r = post.cur_r
			g = post.cur_g
			b = post.cur_b
			pixels.append((r, g, b))
		client.put_pixels(pixels, channel=4)


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
