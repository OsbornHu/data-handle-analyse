import tushare as ts

#http://tushare.org/trading.html#id2

df = ts.get_realtime_quotes('002905')            #当日的历史分笔数据
print(df.head(10) )                                #距离执行时间最近的10笔
df = ts.get_realtime_quotes('000725')            #当日的历史分笔数据
print(df.head(10) )                                #距离执行时间最近的10笔
df = ts.get_realtime_quotes('002475')            #当日的历史分笔数据
print(df.head(10) )                                #距离执行时间最近的10笔
df = ts.get_realtime_quotes('002565')            #当日的历史分笔数据
print(df.head(10) )                                #距离执行时间最近的10笔
df = ts.get_realtime_quotes('600690')            #当日的历史分笔数据
print(df.head(10) )                                #距离执行时间最近的10笔

df = ts.get_realtime_quotes(['sh','sz'])
print(df.head(10) )
#上证指数 深圳成指 沪深300指数 上证50 中小板 创业板
#ts.get_realtime_quotes(['sh','sz','hs300','sz50','zxb','cyb'])

