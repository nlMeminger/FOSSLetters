from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
from bfgmagicletters.views import create_post
import sys, webcolors, re, requests
from urllib.request import urlopen
from urllib.parse import urlencode
from django.views.decorators.csrf import csrf_exempt

letters = ['M', 'A', 'G', 'I', 'C']
rgb = r"(\d+),\s*(\d+),\s*(\d+)"
@csrf_exempt
def sms_response(request):
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
    create_post(post_data)
    #result = urlopen('http://magicletters.kylesuero.com/letter_update', urlencode(post_data))
    #create_post(requests.post('http://magicletters.kylesuero.com/letter_update/', data = {'method':'POST','letter':'M', 'cur_r':'255', 'cur_g':'0', 'cur_b':'0'}))
