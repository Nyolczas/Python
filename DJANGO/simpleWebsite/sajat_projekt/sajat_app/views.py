from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dictionary = {'insert_me' : "Hello én már a pythonból jöttem!"}
    #ez küldi vissza
    return render(request, 'sajat_app/index.html',context=my_dictionary)

def help(request):
    helpdict = {'help_content' : 'Ez a segítség már a PYTHONBÓL gyütt!'}
    return render(request,'sajat_app/help.html',context=helpdict)  
