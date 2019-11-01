import tushare as ts

#http://tushare.org/trading.html#id2

df = ts.get_realtime_quotes('002905')            #当日的历史分笔数据
print(df.head(10) )                                #距离执行时间最近的10笔
df = ts.get_realtime_quotes('000725')            #当日的历史分笔数据
print(df.head(10) )                                #距离执行时间最近的10笔
df = ts.get_realtime_quotes('600438')            #当日的历史分笔数据
print(df.head(10) )                                #距离执行时间最近的10笔
df = ts.get_realtime_quotes('002475')            #当日的历史分笔数据
print(df.head(10) )                                #距离执行时间最近的10笔
df = ts.get_realtime_quotes('002446')            #当日的历史分笔数据
print(df.head(10) )                                #距离执行时间最近的10笔


