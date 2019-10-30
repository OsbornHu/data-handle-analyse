import tushare as ts


basic = ts.get_stock_basics()
basic_pe = basic[(basic.pe<10)&(basic.pe!=0)]
print(basic_pe)