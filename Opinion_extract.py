!mkdir data
from pandas.core.indexes.interval import IntervalIndex
import pandas as pd
import seaborn as sns
%matplotlib inline
import pylab
import numpy as np
import matplotlib
%matplotlib inline
import random
import matplotlib.pyplot as plt
# make the plots a little wider by default
%matplotlib inline
plt.style.use('ggplot')
pylab.rcParams['figure.figsize'] = (10., 8.)

data = pandas.read_csv('google_data.csv')
data.head()
