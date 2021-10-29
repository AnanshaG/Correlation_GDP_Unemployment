""" This code predicts the gdp rate and upemployment rate, we can see their is
negative correlation between both the parameters."""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = np.array(pd.read_csv(r'data.csv'))
#print(data)
unemp_rate = data[:-2,1]
gdp_rate1 = data[:-2,2]
#print(gdp_rate1)
n = len(gdp_rate1)
gdp_rate = gdp_rate1.reshape(n,1)
#print(gdp_rate)
lr = LinearRegression()
plt.plot(gdp_rate1, unemp_rate)
plt.show()
trained = lr.fit(gdp_rate, unemp_rate)
x = [[6.54],[-23.9]]
res = trained.predict(x)
print(res)
#g = list(res)
#plt.plot(gdp_rate1,res,'^')
#plt.show()
