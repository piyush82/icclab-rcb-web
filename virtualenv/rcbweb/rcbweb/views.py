############################################################
#@author: Piyush Harsh (piyush.harsh@zhaw.ch)
#@version: 0.1
#@summary: Django project implementing RCB Web Interface
#
#@requires: django 1.6.0+
############################################################

from django.shortcuts import render
import datetime

def index(request):
    now = datetime.datetime.now()
    #to_display = "Hello World! The time here is now %s. The extra parameter received is: %s" % (now, options)
    to_display = "We are located in Winterthur, local time here is %s." % (now)
    #creating a dictionary to send
    data = {}
    data['title'] = 'Welcome to my Test Site!'
    data['content'] = to_display
    
    return render(request, 'index.html', {'data':data})

def login(request):
    data = {}
    return render(request, 'base.html', {'data':data})

def worker(request, options):
    data = {}
    return render(request, 'base.html', {'data':data})