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

opinion = pandas.read_csv('opinion_data.csv')
opinion.head()

#?Create relative row and column for each states, including happening, worried, futuregen, harmUS, personal
opinion1 = pd.DataFrame(np.random.randn(1,5))
opinion1 = pd.DataFrame()
opinion1.columns = ['happening','worried','futuregen','harmUS','personal']
opinion1.index = ['Alabama', 'Alaska', 'Arizona','Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia',
                  'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 
                  'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
                  'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
                  'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
opinion1

#? Create a new file contain the average of opinion index




