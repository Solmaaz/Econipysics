#Econipysics_correlation 
#Solmaz Golmohammadi

import pandas as pd
import pandas_datareader as pdr 
import matplotlib.pyplot as plt 
import seaborn as sns
import os 

aapl =pdr.get_data_yahoo('AAPL', '2019-05-04')
aapl.head()
aapl.to_csv('AAPL', index=True)

nok =pdr.get_data_yahoo('NOK', '2019-05-04')
nok.head()
nok.to_csv('NOK', index=True)

bb =pdr.get_data_yahoo('BB', '2019-05-04')
bb.head()
bb.to_csv('BB', index=True)

path = '/home/solmaz/Desktop/econiphysics/Stock'
names= os.listdir(path)
#print(names)
#names = names[:3]
#print(names)
df_main =pd.DataFrame()
for name in names:
    add = os.path.join(path,name)
    df= pd.read_csv(add,index_col=0)
    df.drop({'High','Low','Open','Close','Volume'}, axis=1,inplace= True)
    df=df.rename(columns={'Adj Close':name})
    df_main = df_main.join(df, how='outer')
df_corr = df_main.corr()    
sns.heatmap(df_corr, Cmap= 'RdYlGn')
plt.show()