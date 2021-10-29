import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
def correlation(x,y,n):
    """ This function calculates the correlation between two parameters, x is parameter one, y is second parameter, n is total rows. """
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x2 = 0
    sum_y2 = 0
    i = 0
    while i < n:
        sum_x = sum_x + x[i]
        sum_y = sum_y + y[i]
        sum_xy = sum_xy + x[i] * y[i]
        sum_x2 = sum_x2 + x[i] * x[i]
        sum_y2 = sum_y2 + y[i] * y[i]
        i = i+1
        corr = (float)(n * sum_xy - sum_x * sum_y)/(math.sqrt((n * sum_x2 - sum_x * sum_x) * (n * sum_y2 - sum_y * sum_y)))
    return corr

data = np.array(pd.read_csv(r'data.csv'))
#print(data)
unemp_rate = data[:-2,1]
gdp_rate = data[:-2,2]
n = len(gdp_rate)
print(unemp_rate)
print(gdp_rate)
print('{0:6f}'.format(correlation(gdp_rate,unemp_rate,n)))
plt.plot(gdp_rate,unemp_rate,"^")
plt.xlabel("gdp rate")
plt.ylabel("unemployement rate")
plt.title("Corelation Graph between gdp and unemployement rate 2019")
plt.show()


