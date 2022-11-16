# Requirments
#---------------------------

from crawler import *
import pickle
import pandas as pd
pd.set_option('display.max_columns', None)
#import datetime as dt


# Load & SAVE
#---------------------------
data = collector(year='2022', gender='t', page='max')
pickle.dump(data, open('name_all_2022.pkl', 'wb'))
#data = pickle.load(open('name_all_2022.pkl', 'rb'))


# Test
#---------------------------

cols = data[0].columns
print(cols)

for i in range(len(cols)):
    print(type(data[0].iloc[0,i]))

