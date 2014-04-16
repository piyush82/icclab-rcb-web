############################################################
#@author: Piyush Harsh (piyush.harsh@zhaw.ch)
#@version: 0.1
#@summary: Django project implementing RCB Web Interface
#
#@requires: django 1.6.0+
############################################################

from django.shortcuts import render
from rcbweb.models import LoginForm
from rcbweb.models import RegistrationForm
from django.http import HttpResponse
from django.template import RequestContext

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
    form = LoginForm()
    data['content'] = form.as_table()
    #data['content'] = form.as_p()
    #data['content'] = form.as_ul()
    return render(request, 'gatekeeper.html', {'data':data})

def worker(request, options):
    #print options
    if options == 'register':
        form = RegistrationForm()
        form.fields['osuser'].label = "OpenStack Username"
        form.fields['ospassword'].label = "OpenStack Password"
        form.fields['ostenantname'].label = "OpenStack Tenant Name"
    data = {}
    data['title'] = 'ICCLab RCB Engine: Registration'
    data['content'] = form.as_table()
    return render(request, 'registration.html', {'data':data})

def doaction(request, options):
#     print options
    if options == 'doregistration':
        if request.method == 'POST':
            formData =  request.POST.dict()
            isValid, errorList = validate(formData, "registration")
            if isValid:
                print 'Valid Form data received'
            else:
                print 'Something fishy is going on'
    data = {}
    return render(request, 'status.html', {'data':data})

def validate(values, validationType):
    status = False
    fList = []
    return status, fList
