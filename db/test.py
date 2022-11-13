from crawler import *
import pandas as pd
pd.set_option('display.max_columns', None)
#import datetime as dt



### Test
data = collector(year='2022', gender='t', page='max')
print(len(data))
print(data[0].head())
