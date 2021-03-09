from django.shortcuts import render,redirect
import sys,os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import seaborn as sns
import numpy as np
import csv
import math
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
from io import StringIO
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from django.http import HttpResponse
import mpld3
import urllib,base64

#from simi import ret_graph
from .models import blog,datasets,team

blogId = ''

# Create your views here.

context = {}

def title(request):
    return HttpResponse("Home Page")

def Overview(request):
    my_de = {'Over_tag':'\0'}
    blogs = blog.objects.all()
    if request.method == 'POST':
    		global blogId
    		blogId = request.POST['blogId']
    		#print("Overview")
    		#print(blogId)
    return render(request,'overview.html',{'blogs':blogs})

def Main(request):
    return HttpResponse("Main")

def dataset(request):
   my_data = {'Data_tag':'\0'}
   if request.method == 'POST':
   		url1 = request.POST['url1']
   		url2 = request.POST['url2']
   		print(url1)
   		print(url2)
   		return redirect('sim')
   return render(request,'simgen.html', context = my_data)

def home(request):
    my_home = {'home_tag':'\0'}
    return render(request,'home.html',context = my_home)

def about(request):
	#print(os.getcwd())
	members = team.objects.all()
	return render(request,'aboutus.html',{'members':members})

def learnmore(request):
	#print("learnmore")
	#print(blogId)
	req_blog = blog.objects.get(id=int(blogId))
	return render(request,'display.html',{'req_blog':req_blog})

def sim_graph(request):
#	context['graph'] = ret_graph()
	#print(datasets.path)
	dataset = datasets.objects.get(id=1)
	path = getattr(dataset,'path')
	df1 = pd.read_csv(path,parse_dates=["timestamp"], index_col="timestamp")

	print(df1)
	df1[df1.columns].plot(kind='line')
	fig = plt.gcf()

	buf = io.BytesIO()
	fig.savefig(buf,format='png')
	buf.seek(0)
	string = base64.b64encode(buf.read())
	uri = urllib.parse.quote(string)

	df1_resample = df1[df1.columns].resample('D').mean()
	df1_resample = df1_resample.interpolate()
	df1_resample.plot(kind='line',figsize=(20,10))
	fig = plt.gcf()

	buf = io.BytesIO()
	fig.savefig(buf,format='png')
	buf.seek(0)
	string = base64.b64encode(buf.read())
	uri2 = urllib.parse.quote(string)

	return render(request,'simi.html',{'data':uri, 'data2':uri2})

#def login(request):
#    my_login = {'login_tag':'\0'}
#    return render(request,'App/login.html',context = my_login)
