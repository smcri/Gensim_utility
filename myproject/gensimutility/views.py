from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def title(request):
    return HttpResponse("Home Page")

def Overview(request):
    my_de = {'Over_tag':'\0'}
    return render(request,'overview.html',context=my_de)

def Main(request):
    return HttpResponse("Main")

def dataset(request):
   my_data = {'Data_tag':'\0'}
   return render(request,'datasets.html', context = my_data)

def home(request):
    my_home = {'home_tag':'\0'}
    return render(request,'home.html',context = my_home)

#def login(request):
#    my_login = {'login_tag':'\0'}
#    return render(request,'App/login.html',context = my_login)
