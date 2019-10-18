import tushare as ts

#获取实时行情数据get_today_all()
#返回值说明：code：代码 name:名称 changepercent:涨跌幅 trade:现价  open:开盘价  high:最高价  low:最低价
# settlement:昨日收盘价 volume:成交量  turnoverratio:换手率  amount:成交量  per:市盈率  pb:市净率  mktcap:总市值 nmc:流通市值

#ts.get_today_all()
df = ts.get_realtime_quotes('002905')            #当日的历史分笔数据
print(df.head(10) )                                #距离执行时间最近的10笔

df = ts.get_realtime_quotes('000725')            #当日的历史分笔数据
print(df.head(10) )                                #距离执行时间最近的10笔
#data=ts.get_hist_data('002905')
#print(data.info)
#获取历史分笔数据之：get_tick_data()
df=ts.get_tick_data('002905',date='2019-10-11')
print(df)
#df.head(10)

#获取实时指数
ts.get_realtime_quotes('sh')

