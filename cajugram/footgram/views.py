from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def footgram(request):
    template = loader.get_template('my_first.html')
    return HttpResponse(template.render())

    # In this we can:
        #Pull data from a database
        #Transform data
        #Send emails
