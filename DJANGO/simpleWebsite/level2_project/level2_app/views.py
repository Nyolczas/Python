from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {'insert_me' : 'Helló, én a view tartalma vagyok!'}
    return render(request,'level2_app/index.html',context=my_dict)

# Create your views here.
