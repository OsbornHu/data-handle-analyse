import tushare as ts
import hdfs as hdfs
import matplotlib.pyplot as plt

client=hdfs.Client("http://10.108.1.56:50070")  #连接到HDFS服务

df = ts.get_hist_data('002905')

close = df['close']
volume = df['volume']
ma5 = df['ma5']
ma10 = df['ma10']
ma20 = df['ma20']

v_ma5 = df['v_ma5']
v_ma10 = df['v_ma10']
v_ma20 = df['v_ma20']

close.plot(label='close')
ma5.plot(label='ma5')
ma10.plot(label='ma10')
ma20.plot(label='ma20')
plt.legend()
plt.show()

#print(df.head(10) )