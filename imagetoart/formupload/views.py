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
			# Style 1 is the style for person
                    elif 'style1' in request.POST:
                        handle_uploaded_file2(request.FILES['file'], str(request.FILES['file']))                       
			# Style 2 is the style for background
                    elif 'style2' in request.POST:
                        handle_uploaded_file3(request.FILES['file'], str(request.FILES['file']))                       
            return HttpResponse("<h1>Successful Upload ...</h1>")




 
def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')
    with open('upload/input.jpg', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    with open('/home/ubuntu/input.jpg', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    #added to transfer filename
   # messages.add_message(request, messages.INFO, form.cleaned_data['name'])
   #  return HttpResponseRedirect('/submit/')       


#person styloe upload
def handle_uploaded_file2(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')
    with open('upload/style1.jpg', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    #added to transfer filename
   # messages.add_message(request, messages.INFO, form.cleaned_data['name'])
   #  return HttpResponseRedirect('/submit/')       

#background style upload
def handle_uploaded_file3(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')
    with open('upload/style2.jpg', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)




###################################################
   ###### STYLE IMAGE
   #######################################



   ###################
   ###################


#Kick off image processing
def submit(request): 
        if (request.method == 'POST'):
        	if 'create' in request.POST:
			with open("/home/ubuntu/style-transfer-master/outputfile_path","a+") as out:
				#f = open("/home/ubuntu/style-transfer-master/outputfile_path","a+")
				#f.flush()

				process = subprocess.Popen([sys.executable,'-u','/home/ubuntu/style-transfer-master/style.py','-s','/home/ubuntu/imagetoart/upload/style1.jpg','-c','/home/ubuntu/imagetoart/upload/input.jpg', '-n', '512','-m','vgg16','-g','0','-o','/home/ubuntu/style-transfer-master/outputs/style_person.jpg'])
				process = subprocess.call([sys.executable,'-u','/home/ubuntu/style-transfer-master/style.py','-s','/home/ubuntu/imagetoart/upload/style2.jpg','-c','/home/ubuntu/imagetoart/upload/input.jpg','-n','512','-m','vgg16','-g','0','-o','/home/ubuntu/style-transfer-master/outputs/style_background.jpg'])
				#for line in process.stdout:
				#	sys.stdout.write(line)
				#	logfile.write(line)
        			time.sleep(20)

				process = subprocess.check_call([sys.executable,'-u','/home/ubuntu/crfasrnn-master/python-scripts/crfasrnn_demo.py'], cwd='/home/ubuntu/crfasrnn-master/python-scripts')
				#return HttpResponse("<h1>Processing Data....</h1>")
        	#elif 'check' in request.POST:
				if (os.path.isfile("/home/ubuntu/output.jpg")):
					image_data = open("/home/ubuntu/output.jpg", "rb").read()
					return HttpResponse(image_data, content_type="image/png")
				else:
				#log = open("/home/ubuntu/style-transfer-master/outputfile_path", "rb").read()
            				return HttpResponse("<h1>Processing image....please wait...</h1>")
				#log = open("/home/ubuntu/style-transfer-master/hellosteve", "rb").read()
				#"<h1>Sorry, Image not ready yet, See console for ETA. Go Back</h1>")
				#return HttpResponse(log, content_type='text/plain')
        	elif 'reset' in request.POST:

				os.system("rm /home/ubuntu/input.jpg")
				os.system("rm /home/ubuntu/imagetoart/upload/input.jpg /home/ubuntu/imagetoart/upload/style1.jpg /home/ubuntu/imagetoart/upload/style2.jpg")
				os.system("rm /home/ubuntu/style-transfer-master/outputs/style_background.jpg /home/ubuntu/style-transfer-master/outputs/style_person.jpg")
				os.system("rm /home/ubuntu/output.jpg")
       				return HttpResponse("<h1>Image Locations Reset</h1>")

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


