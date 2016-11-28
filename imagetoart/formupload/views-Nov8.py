import sys
import os
import os.path
import time
import datetime
import subprocess
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.messages import get_messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.generic import View
from django import forms


def print_http_response(f):
# Courtesy Chase Seibert
# http://chase-seibert.github.io/blog/2010/08/06/redirect-console-output-to-a-django-httpresponse.html
    """ Wraps a python function that prints to the console, and
    returns those results as a HttpResponse (HTML)"""

    class WritableObject:
        def __init__(self):
            self.content = []
        def write(self, string):
            self.content.append(string)

    def new_f(*args, **kwargs):
        printed = WritableObject()
        sys.stdout = printed
        f(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return HttpResponse(['<BR>' if c == '\n' else c for c in printed.content ])
    return new_f



# help from
# http://stackoverflow.com/questions/24042669/using-data-from-one-view-function-in-another-with-django-forms
# Create your views here.



def submit2(request):
    #def post(self, request, *args, **kwargs):
        execfile('dummy.py')
        #os.system(python print "exucting script...this is a test")
     #   return HttpResponse()

    
def home(request):
    return render(request, 'index.htm', {'what':'CodePlay Image to Art Conversion Tool'})

###################################################
   ###### CONTENT IMAGE
   #######################################
 

def upload(request):
            #filecontent = request.FILES['file']
            if (request.method == 'POST'):
                    if 'content' in request.POST:
                        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
                    elif 'style' in request.POST:
                        handle_uploaded_file2(request.FILES['file'], str(request.FILES['file']))                       
            return HttpResponse("<h1>Successful Upload ...</h1>")




 
def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')
    with open('upload/content.jpg', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    #added to transfer filename
   # messages.add_message(request, messages.INFO, form.cleaned_data['name'])
   #  return HttpResponseRedirect('/submit/')       


def handle_uploaded_file2(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')
    with open('upload/style.jpg', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    #added to transfer filename
   # messages.add_message(request, messages.INFO, form.cleaned_data['name'])
   #  return HttpResponseRedirect('/submit/')       





###################################################
   ###### STYLE IMAGE
   #######################################



   ###################
   ###################


#Kick off image processing
def submit(request): 
        if (request.method == 'POST'):
        	if 'create' in request.POST:
			subprocess.Popen([sys.executable,'/home/ubuntu/style-transfer-master/style.py','-s','/home/ubuntu/imagetoart/upload/style.jpg','-c','/home/ubuntu/imagetoart/upload/content.jpg','-m','vgg16','-g','-1','-o','/home/ubuntu/style-transfer-master/outputs/test_nanjing.jpg',stdout=/home/ubuntu/style-transfer-master/outputfile])
			return HttpResponse("<h1>Processing....Please wait and Click Check Status Button on main page.  Thank You!</h1>")
        	elif 'check' in request.POST:
			if (os.path.isfile("/home/ubuntu/style-transfer-master/outputs/test_nanjing.jpg")):
				image_data = open("/home/ubuntu/style-transfer-master/outputs/test_nanjing.jpg", "rb").read()
				return HttpResponse(image_data, content_type="image/png")
			else:
				#"<h1>Sorry, Image not ready yet, See console for ETA. Go Back</h1>")
				fsock = open("/home/ubuntu/style-transfer-master/outputfile_path","rb")
				return HttpResponse(fsock, content_type='text/plain')
	return HttpResponse("")





    #sys.argv = ['/home/ubuntu/style-transfer-master/style.py','-s','/home/ubuntu/imagetoart/upload/style.jpg','-c','/home/ubuntu/imagetoart/upload/content.jpg','-m','vgg16','-g','-1','-o','/home/ubuntu/style-transfer-master/outputs/test_nanjing.jpg']
    #execfile('/home/ubuntu/style-transfer-master/style.py')

    #while not os.path.isfile("/home/ubuntu/style-transfer-master/outputs/test_nanjing.jpg"):
        #print "Time is " + time.ctime()
        #time.sleep(10)
	#HttpResponse("Processing image ...")

    #while not os.path.exists("/home/ubuntu/style-transfer-master/outputs/"):
    #    HttpResponse("Processing image ...")
    #    time.sleep(1)




   




def myview(request):
    file = request.FILES['file1'] # this is my file

  #  file = request.FILES['filename']
#file.name           # Gives name
#file.content_type   # Gives Content type text/html etc
#file.size           # Gives file's size in byte
#file.read()         # Reads file


