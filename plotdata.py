#!/home/biff/notebook/jupyterenv/bin/python3

from pandas import read_csv
from pandas import set_option
from matplotlib import pyplot

#path = r"secure.csv"
path = r"secure2.csv"
headernames=['dow','month','day','time','TZ','year','user','IP','country']
data = read_csv(path, names=headernames)
print(data.head(50))

print(data.shape)
print(data.dtypes)
set_option('display.width', 100)
#set_option('precision', 2)
print(data.describe())
data.hist()
pyplot.show()
data.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
pyplot.show()
