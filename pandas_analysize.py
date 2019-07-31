import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file = open('cast_netengine.log')
data = []

for line in file.readlines():
	data.append(float(line.strip())/1000)
data.sort()

border = 2500
data1 = [x for x in data if x<border]
n,bins,patches = plt.hist(data1,bins=30)
plt.xlim(min(data1),max(data1))
plt.xlabel('range')
plt.ylabel('count')
plt.title(u'cast(us)')
plt.grid(True)
plt.savefig('./below_2.5ms.png')



data2 = [x for x in data if x>=border]
n,bins,patches = plt.hist(data2,bins=20)
plt.xlim(min(data2),max(data2))
plt.xlabel('range')
plt.ylabel('count')
plt.title(u'cast(us)')
plt.grid(True)
plt.savefig('./above_2.5ms.png')


row = []
row.append(round(np.mean(data),2))
row.append(max(data))
row.append(min(data))
row.append(round(np.std(data,ddof=1),2))
row.append(data[int(len(data)/10)])
row.append(data[int(len(data)/2)])
row.append(data[int((len(data) * 9)/10)])
index = [u'时延']
columns = [u'平均值',u'最大值',u'最小值',u'标准差',u'十分位',u'中位数',u'十分之九分位']

df = pd.DataFrame([row],index=index,columns=columns)
print(df.describe())
