''' Does a simple linear regression plot
depends on statsmodels and pandas and patsy

See http://pandas.pydata.org/pandas-docs/stable/visualization.html for more details on pandas plotting
See http://statsmodels.sourceforge.net/stable/index.html for details on statsmodels
Regression http://pandas.pydata.org/pandas-docs/dev/computation.html
time series http://pandas.pydata.org/pandas-docs/stable/timeseries.html
This is for reference not actual use.
'''
import pandas as pd
from pd import DataFrame, Series
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import statsmodels

def insert_trendline(df, model):
    df['regr'] = df.index*model.beta[0] + model.beta[1]
    return df

def labl(axis):
    a = axis
    a.set_ylabel('European MobilePhone Subscriptions (millions)')
    a.set_xlabel('Year')
    a.set_title('European Mobile Phone Trend')
    return a


df = pd.read_csv(csv_path)
start_year = datetime(1999,1,1)
end_year = datetime(2009,1,1)
years = pd.date_range(start_year,end = end_year, freq='A')
#using a data column as an index
col_ind = 'years'
ds = ds.set_index(col_ind)
ds = ds.reset_index()
column_name = 'measured'
model = pd.ols(y=ds[column_name], x=ds.ix[:,'index'])
model.beta #the linear regression model
model.beta.plot() # plots the trend line alone
plt.show()
column_list = ['regr', column_name]
ds[column_list].plot()
ext = DataFrame(ds, index = range(22))
R = insert_trendline(ext, model)
R = insert_trendline(ext, model).set_index('index')
norm_factor = 1000
data = R[column_list]/norm_factor
A = data.plot()
labl(A)
plt.show()
