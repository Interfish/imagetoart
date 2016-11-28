import os
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




class MyValidationForm(forms.Form):
    first = forms.CharField()
    second = forms.IntegerField()
    third = forms.IntegerField()

    
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
                        print "post 1"
                        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
                    elif 'style' in request.POST:
                        print "post 2"
                        handle_uploaded_file2(request.FILES['file'], str(request.FILES['file']))                       
            return HttpResponse("Successful ...")




 
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










def submit(request):
    execfile('style.py -s ./images/style/starry_night.jpg -c ./images/content/nanjing.jpg -m vgg16 -g -1 -o ./outputs/test_nanjing.jpg')
    return HttpResponse("Running Script.....")
    #storage = get_messages(request)
    #name = file.name
   # if request.FILES['filename'].name
         
    #for filename, file in request.FILES.iteritems():
     #       name = request.FILES[filename].name


   




def myview(request):
    file = request.FILES['file1'] # this is my file

  #  file = request.FILES['filename']
#file.name           # Gives name
#file.content_type   # Gives Content type text/html etc
#file.size           # Gives file's size in byte
#file.read()         # Reads file




