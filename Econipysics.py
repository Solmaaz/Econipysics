#Econipysics 
#Solmaz Golmohammadi

import pandas as pd
import pandas_datareader as pdr 
import matplotlib.pyplot as plt 
import seaborn as sns

aapl =pdr.get_data_yahoo('AAPL', '2019-05-04')
aapl.head()
df= aapl['Adj Close']
df.head()
EMA =df.ewm(com=0.5).mean()
print(EMA.head())
EMA.to_csv(r'ema.txt', header=None, index=True, sep=' ')
df.to_csv(r'close-prices.txt', header=None, index=True, sep=' ')
sns.distplot(df)
plt.show()
Mean = df.mean()
print("Mean value = ")
print(Mean)
Std = df.std()
print("Standard deviation = ")
print(Std)
skewnes = df.skew()
print("Skewnes = ")
print(skewnes)
kurtosis = df.kurtosis()
print("Kurtosis = ")
print(kurtosis)
