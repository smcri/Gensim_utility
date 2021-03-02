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


df1 = pd.read_csv("https://raw.githubusercontent.com/scikit-multiflow/streaming-datasets/master/iris_timestamp.csv",parse_dates=["timestamp"], index_col="timestamp")

print(df1)

def ret_graph():

	fig = Figure()
	canvas = FigureCanvas(fig)
	df1[df1.columns].plot(kind='line')
	buf = io.BytesIO()
	plt.savefig(buf, format='png')
	plt.close(fig)	
	response = HttpResponse(content_type = 'image/jpg')
	canvas.print_jpg(response)
	return response