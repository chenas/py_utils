import pandas as pd
import matplotlib.pyplot as plt

papa=pd.read_csv('cast20190727_250.txt',sep=' ')
sections=[0, 10000, 15000, 20000, 25000, 30000, 100000000]
group_names=['0-10k', '10k-15k', '15k-20k', '20k-25k', '25k-30k', '30+']
cuts=pd.cut(papa['6'], sections,labels=group_names)
plt.figure()
''' cuts.value_counts().plot(kind='bar') '''
cuts.value_counts(normalize=True).plot(kind='pie', figsize=(6,6), autopct='%0.2f', title='client-server cast')
plt.show()
