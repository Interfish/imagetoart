import os
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
print "python style.py -s ./images/style/starry_night.jpg -c ./images/content/nanjing.jpg -m vgg16 -g -1 -o ./outputs/test_nanjing.jpg"
