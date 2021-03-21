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
from django.core.validators import URLValidator

#from simi import ret_graph
from .models import blog,datasets,team

validate = URLValidator()

blogId = ''
url1 = ''
url2 = ''

# Create your views here.


context = {}

def norm(x):
    square = [number**2 for number in x]
    Sum = sum(square)
    return math.sqrt(Sum)

def cosine(x,y,path):
	prod = 0
	for i in path:
		prod = prod + x[i[0]]*y[i[1]]
	return prod/(norm(x)*norm(y))
            

def eucli(x,y,path):
	sume = 0
	for i in path:
		sume = sume + abs(x[i[0]] - y[i[1]])**2
	return math.sqrt(sume)

def pearson(x,y,path):
	sump = 0
	for i in path:
		sump = sump + ((x[i[0]] - y[i[1]])**2)/y[i[1]]
	return sump

def chebyshev(x,y,path):
	max = abs(x[1] - y[1])
	for i in path:
		if(abs(x[i[0]] - y[i[1]])>max):
			max = abs(x[i[0]] - y[i[1]])
	return max

def soergel(x,y,path):
	sum1 = 0
	sum2 = 0
	for i in path:
		sum1 = sum1 + abs(x[i[0]] - y[i[1]])
		sum2 = sum2 + max(x[i[0]],y[i[1]])
	return sum1/sum2

def kulcynski(x,y,path):
	sum1 = 0
	sum2 = 0
	for i in path:
		sum1 = sum1 + abs(x[i[0]] - y[i[1]])
		sum2 = sum2 + min(x[i[0]],y[i[1]])
	return sum1/sum2

def matusita(x,y,path):
	summ = 0
	for i in path:
		summ = summ + (math.sqrt(math.fabs(x[i[0]])) - math.sqrt(math.fabs(y[i[1]])))**2
	return math.sqrt(summ)

def divergence(x,y,path):
	sum1 = 0
	sum2 = 0
	for i in path:
		sum1 = sum1 + (x[int(i[0])]- y[int(i[1])])**2
		sum2 = sum2 + (x[int(i[0])]+ y[int(i[1])])**2
	return 2*(sum1/sum2)

def graphrender(buf):
	fig.savefig(buf,format='png')
	buf.seek(0)
	string = base64.b64encode(buf.read())
	return string

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
   dataset_set = datasets.objects.all()
   if request.method == 'POST':
   		global url1
   		global url2
   		url1 = request.POST['dset1']
   		url2 = request.POST['dset2']
   		print(url1)
   		print(url2)
   		try:
   			validate(url1)
   			print("String is a valid URL")
   		except:
   			tempo = url1
   			print(tempo)
   			tempo2 = datasets.objects.get(name=tempo)
   			url1 = getattr(tempo2,'path')
   			print("String is not a valid URL")

   		try:
   			validate(url2)
   			print("String is a valid URL")
   		except:
   			tempo = url2
   			tempo2 = datasets.objects.get(name=tempo)
   			url2 = getattr(tempo2,'path')
   			print("String is not a valid URL")


   		return redirect('sim')
   return render(request,'simgen.html', {'dataset_set':dataset_set})

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
	global fig
	global distance


	dataset = datasets.objects.get(id=1)
	path1 = getattr(dataset,'path')
	df1 = pd.read_csv(url1,parse_dates=True, index_col=0)

	print(df1)
	df1[df1.columns].plot(kind='line')
	fig = plt.gcf()

#	buf = io.BytesIO()
#	fig.savefig(buf,format='png')
#	buf.seek(0)
#	string = base64.b64encode(buf.read())
	uri = urllib.parse.quote(graphrender(io.BytesIO()))

	plt.clf()

#	df1.plot(kind='bar')
#	fig = plt.gcf()
#	uri110 = urllib.parse.quote(graphrender(io.BytesIO()))
#	plt.clf()

	
	l = 1
	r = 365*24
	ans = l
	while l<=r:
		mid = int((l+r)/2)
		df1_resample = df1[df1.columns].resample(str(mid)+'H').mean()
		sz = int(len(df1_resample))
		print(sz)
		if sz<=150:
			ans = sz
			r = mid-1
		elif sz>150:
			l = mid+1

#	df1_resample = df1[df1.columns].resample('D').mean()
	df1_resample = df1_resample.interpolate()
	df1_resample.plot(kind='line',figsize=(20,10))
	fig = plt.gcf()

#	buf = io.BytesIO()
#	fig.savefig(buf,format='png')
#	buf.seek(0)
#	string = base64.b64encode(buf.read())
	uri2 = urllib.parse.quote(graphrender(io.BytesIO()))

	plt.clf()

	df1_resample.plot(kind='bar',figsize=(20,10))
	fig = plt.gcf()

#	buf = io.BytesIO()
#	fig.savefig(buf,format='png')
#	buf.seek(0)
#	string = base64.b64encode(buf.read())
	uri3 = urllib.parse.quote(graphrender(io.BytesIO()))

	plt.clf()

	matrix_corr = df1_resample.corr()
	ax = sns.heatmap(
    matrix_corr, 
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True)

	ax.set_xticklabels(ax.get_xticklabels(),rotation=45,horizontalalignment='right')
	fig = plt.gcf()

	uri4 = urllib.parse.quote(graphrender(io.BytesIO()))

	plt.clf()

	df1_resample_combine = df1_resample.take([1],axis=1)
	for i in range(len(df1_resample)):
		df1_resample_combine[i:i+1] = np.average(df1_resample[i:i+1],axis=1, weights=(1*df1_resample.var()+0.0*df1_resample.mean()))
	df1_resample_combine.plot(kind='line',figsize=(20,10))
	fig = plt.gcf()

	uri5 = urllib.parse.quote(graphrender(io.BytesIO()))

	plt.clf()

#	df1_resample_combine.plot(kind='bar',figsize=(20,10))
#	fig = plt.gcf()

#	uri112 = urllib.parse.quote(graphrender(io.BytesIO()))

#	plt.clf()

#	desc = df1_resample.describe()
#	fig2,ax = plt.subplots()
#	ax.table(cellText=desc.values, colLabels=desc.keys(), loc='center')
#	fig = plt.gcf()
#	uri113 = urllib.parse.quote(graphrender(io.BytesIO()))
#	plt.clf()

	dataset = datasets.objects.get(id=2)
	path1 = getattr(dataset,'path')
	df2 = pd.read_csv(url2,parse_dates=True,index_col=0)

	df2[df2.columns].plot(kind='line')
	fig = plt.gcf()

	uri6 = urllib.parse.quote(graphrender(io.BytesIO()))

	plt.clf()

#	df2.plot(kind='bar')
#	fig = plt.gcf()
#	uri220 = urllib.parse.quote(graphrender(io.BytesIO()))
#	plt.clf()

#	matrix_corr = df2.corr()
#	ax = sns.heatmap(matrix_corr, vmin=-1, vmax=1, center=0,cmap=sns.diverging_palette(20, 220, n=200),square=True)
#	ax.set_xticklabels(ax.get_xticklabels(),rotation=45,horizontalalignment='right');
#	fig = plt.gcf()
#	uri221 = urllib.parse.quote(graphrender(io.BytesIO()))
#	plt.clf()


	
	l = 1
	r = 365*24
	ans = l
	while l<=r:
		mid = int((l+r)/2)
		df2_resample = df2[df2.columns].resample(str(mid)+'H').mean()
		sz = int(len(df2_resample))
		print(sz)
		if sz<=150:
			ans = sz
			r = mid-1
		elif sz>150:
			l = mid+1

#	df2_resample = df2[df2.columns].resample('1H').mean()
	df2_resample = df2_resample.interpolate()
	df2_resample.plot(kind='line',figsize=(20,10))
	fig = plt.gcf()

	uri7 = urllib.parse.quote(graphrender(io.BytesIO()))

	plt.clf()

	df2_resample.plot(kind='bar',figsize=(20,10))
	fig = plt.gcf()

	uri8 = urllib.parse.quote(graphrender(io.BytesIO()))

	plt.clf()

	plt.clf()

	matrix_corr = df2_resample.corr()

	ax = sns.heatmap(matrix_corr, vmin=-1, vmax=1, center=0,cmap=sns.diverging_palette(20, 220, n=200),square=True)
	ax.set_xticklabels(ax.get_xticklabels(),rotation=45,horizontalalignment='right');
	fig = plt.gcf()

	uri9 = urllib.parse.quote(graphrender(io.BytesIO()))

	plt.clf()

	#plt.clf()

	#flights = sns.load_dataset("flights")
	#flights = flights.pivot("month", "year", "passengers")
	#ax = sns.heatmap(flights)
	#fig = plt.gcf()

	#uri10 = urllib.parse.quote(graphrender(io.BytesIO()))

	df2_resample_combine = df2_resample.take([1],axis=1)
	for i in range(len(df2_resample)):
		df2_resample_combine[i:i+1] = np.average(df2_resample[i:i+1],axis=1, weights=(1*df2_resample.var()+0*df2_resample.mean()))
	df2_resample_combine.plot(kind='line',figsize=(20,10))
	fig = plt.gcf()
	uri10 = urllib.parse.quote(graphrender(io.BytesIO()))

	plt.clf()

#	df2_resample_combine.plot(kind='bar',figsize=(20,10))
#	fig = plt.gcf()
#	uri222 = urllib.parse.quote(graphrender(io.BytesIO()))
#	plt.clf()

#	desc2 = df2_resample.describe()
#	fig2,ax = plt.subplots()
#	ax.table(cellText=desc2.values, colLabels=desc2.keys(), loc='center')
#	fig = plt.gcf()
#	uri223 = urllib.parse.quote(graphrender(io.BytesIO()))
#	plt.clf()

	
	rowmean2 = np.array(df1_resample_combine)
	rowmean3 = np.array(df2_resample_combine)

	dataset2 = rowmean2
	dataset3 = rowmean3

	distance,path = fastdtw(dataset2, dataset3, dist=euclidean)
	rlen = len(rowmean2) if len(rowmean2)<len(rowmean3) else len(rowmean3)


	cos = cosine(dataset2,dataset3,path)
	euc = eucli(dataset2,dataset3,path)
	pea = pearson(dataset2,dataset3,path)
	cheby = chebyshev(dataset2,dataset3,path)
	soer = soergel(dataset2,dataset3,path)
	kulc = kulcynski(dataset2,dataset3,path)
	matu = matusita(dataset2,dataset3,path)
	dive = divergence(dataset2,dataset3,path)

	return render(request,'result.html',{'data1_line':uri, 'data1resample_line':uri2, 'data1resample_bar':uri3, 'data1resample_corr':uri4, 'data1combined_line':uri5, 'data2_line':uri6, 'data2resample_line':uri7, 'data2resample_bar':uri8, 'data2resample_corr':uri9, 'data2combined_line':uri10, 'cos':cos, 'euc':euc, 'pea':pea, 'cheby':cheby, 'soer':soer, 'kulc':kulc, 'matu':matu, 'dive':dive})

#def login(request):
#    my_login = {'login_tag':'\0'}
#    return render(request,'App/login.html',context = my_login)
