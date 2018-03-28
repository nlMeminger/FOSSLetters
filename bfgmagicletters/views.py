from django.shortcuts import render
from letter.models import Letter
import opc
import color_utils
import time
import math
import sys

def home(request):
	letter_M = Letter.objects.get(letter='M')
	letter_A = Letter.objects.get(letter='A')
	letter_G = Letter.objects.get(letter='G')
	letter_I = Letter.objects.get(letter='I')
	letter_C = Letter.objects.get(letter='C')

	IP_PORT = '127.0.0.1:7890'
	client = opc.Client(IP_PORT)

	n_pixels = 20
	fps = 60

	freq_r = 24
	freq_g = 24
	freq_b = 24

	speed_r = 7
	speed_g = -13
	speed_b = 19

	start_time = time.time()
	while True:
            t = (time.time() - start_time) * 5
            pixels = []
            for ii in range(n_pixels):
                pct = (ii / n_pixels)
                # diagonal black stripes
                pct_jittered = (pct * 77) % 37
                blackstripes = color_utils.cos(pct_jittered, offset=t*0.05, period=1, minn=-1.5, maxx=1.5)
                blackstripes_offset = color_utils.cos(t, offset=0.9, period=60, minn=-0.5, maxx=3)
                blackstripes = color_utils.clamp(blackstripes + blackstripes_offset, 0, 1)
                # 3 sine waves for r, g, b which are out of sync with each other
                r = blackstripes * color_utils.remap(math.cos((t/speed_r + pct*freq_r)*math.pi*2), -1, 1, 0, 256)
                g = blackstripes * color_utils.remap(math.cos((t/speed_g + pct*freq_g)*math.pi*2), -1, 1, 0, 256)
                b = blackstripes * color_utils.remap(math.cos((t/speed_b + pct*freq_b)*math.pi*2), -1, 1, 0, 256)
                pixels.append((r, g, b))
        client.put_pixels(pixels, channel=0)
        time.sleep(1 / fps)
