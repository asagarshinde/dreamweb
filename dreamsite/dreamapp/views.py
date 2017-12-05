from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('dreamapp/index.html')
    return HttpResponse(template.render())

def linux(request):
    template = loader.get_template('dreamapp/linux.html')
    return HttpResponse(template.render())