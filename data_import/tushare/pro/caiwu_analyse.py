import tushare as ts
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import hdfs as hdfs
import copy
from threading import Thread
from pymongo import MongoClient
import json


#https://tushare.pro/document/2?doc_id=36
####链接地址的token,'a82de...............................'这部分是密钥####
pro = ts.pro_api('e401f34dbff435ca4b2107f213ef40816a3f8413e71ebc5378456930')
client=hdfs.Client("http://10.108.1.60:50070",timeout=30000)  #连接到HDFS服务
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# 存储失败列表
fail = []
stock_list = []

class MongoBase:
    def __init__(self,collection):
        self.collection=collection
        self.OpenDB()
    def OpenDB(self):
        user='admin'
        passwd='123456'
        host='10.108.1.57'
        port='27017'
        auth_db='admin'
        uri = "mongodb://"+user+":"+passwd+"@"+host+":"+port+"/"+auth_db+"?authMechanism=SCRAM-SHA-1"
        self.con = MongoClient(uri, connect=False)
        self.db=self.con['thshare']
        self.collection=self.db[self.collection]
    def closeDB(self):
        self.con.close()

def get_profit_data(year1, year2, year3, year4, year5, scode):
    timelist = []
    timelist.append(year1)
    timelist.append(year2)
    timelist.append(year3)
    timelist.append(year4)
    timelist.append(year5)


    roe = []
    net_profit_ratio = []
    gross_profit_rate = []
    net_profits = []
    eps = []
    business_income = []
    bips = []

    for i in timelist:
        profit_data = ts.get_profit_data(i, 4)
        profit_data.index = profit_data.code
        data = profit_data[profit_data.index == scode]

        roe.append(float(data.roe))
        net_profit_ratio.append(float(data.net_profit_ratio))
        gross_profit_rate.append(float(data.gross_profit_rate))
        net_profits.append(float(data.net_profits))
        eps.append(float(data.eps))
        business_income.append(float(data.business_income))
        bips.append(float(data.bips))

    plt.figure(figsize=(12, 6))

    # 营业收入柱状图
    plt.subplot(231)
    ind = np.arange(5)
    plt.bar(ind, business_income, color='yellowgreen')
    plt.title('Business Income(BaiWan Yuan)')
    plt.xticks(ind, (year1, year2, year3, year4, year5))
    for a, b in zip(ind, business_income):
        plt.text(a, b + 0.05, '%.2f' % b, ha='center', va='bottom', fontsize=7)

    # 净利润柱状图
    plt.subplot(232)
    plt.bar(ind, net_profits, color='gold')
    plt.title('Net_profits(Wan Yuan)')
    plt.xticks(ind, (year1, year2, year3, year4, year5))
    for a, b in zip(ind, net_profits):
        plt.text(a, b + 0.05, '%.2f' % b, ha='center', va='bottom', fontsize=7)

    # 每股收益柱状图
    plt.subplot(233)
    plt.bar(ind, eps, color='#FFA500')
    plt.title('EPS')
    plt.xticks(ind, (year1, year2, year3, year4, year5))
    for a, b in zip(ind, eps):
        plt.text(a, b + 0.05, '%.2f' % b, ha='center', va='bottom', fontsize=7)

    # roe折线图
    plt.subplot(234)
    plt.title('ROE(%)')
    plt.plot(roe, 'r', label='ROE')
    plt.xticks(ind, (year1, year2, year3, year4, year5))

    # 净利润率折线图
    plt.subplot(235)
    plt.title('Net_Profit_Ratio(%)')
    plt.plot(net_profit_ratio, 'b', label='Net_Profit_Ratio')
    plt.xticks(ind, (year1, year2, year3, year4, year5))

    # 毛利率折线图
    plt.subplot(236)
    plt.title('Gross_Profit_Rate(%)')
    plt.plot(gross_profit_rate, 'g', label='Gross_Profit_Ratio')
    plt.xticks(ind, (year1, year2, year3, year4, year5))

    plt.show()

#上市公司基本信息
def stock_compay(exch):
    df = pro.stock_company(exchange=exch, fields='ts_code,exchange,chairman,manager,secretary,reg_capital,setup_date,province,city,introduction,website,email,office,employees,main_business,business_scope')
    client.write('/home/hadoop/hive/data/tushare.db/stock_company/'+exch+'.csv', df.to_csv(header=False, index=False, sep=","), encoding='utf-8', overwrite=True)


#业绩预告
def forecast():
    df = pro.forecast(ann_date='20190131', fields='ts_code,ann_date,end_date,type,p_change_min,p_change_max,net_profit_min')
    client.write("/home/hadoop/hive/data/tushare.db/forecast/20190131.csv",
                 df.to_csv(header=False, index=False, sep=","), encoding='utf-8', overwrite=True)

#利润表
def income(exch,num,start_date,end_date):
    th = pro.stock_company(exchange=exch, fields='ts_code')

    # 清空列表
    global fail, stock_list
    fail.clear()
    stock_list.clear()
    stock_list = th['ts_code'].tolist()
    for i in range(num):
        t = Thread(target=incomesingle,args=(start_date,end_date))
        t.start()


def incomesingle(start_date,end_date):
    global fail, stock_list
    while len(stock_list) > 0:
        print("列表剩余[{0}]个元素".format(len(stock_list)))
        # 取出列表中的某个元素
        one = stock_list.pop()
        try:
            print("[{0}]使用get_hist_data方法获取数据".format(one))
            df = pro.income(ts_code=one, start_date=start_date, end_date=end_date,
                            fields='ts_code,ann_date,f_ann_date,end_date,report_type,comp_type,basic_eps,diluted_eps,total_revenue,revenue,int_income,prem_earned,comm_income,n_commis_income,n_oth_income,prem_income,une_prem_reser,n_sec_tb_income,n_sec_uw_income,n_asset_mg_income,oth_b_income,' +
                                   'total_cogs,prem_refund,compens_payout,reser_insur_liab,div_payt,reins_exp,oper_exp,other_bus_cost,operate_profit,total_profit,income_tax,n_income,n_income_attr_p,minority_gain,oth_compr_income,t_compr_income,compr_inc_attr_p,compr_inc_attr_m_s,ebit,ebitda,insurance_exp,undist_profit,distable_profit,update_flag')

            client.write("/home/hadoop/hive/data/tushare.db/income/" + one + ".csv",
                         df.to_csv(header=False, index=False, sep=","), encoding='utf-8', overwrite=True)
        except Exception as e:
            print("[{0}]存储失败,[{1}]".format(one, e))
            fail.append(one)


#资产负债表
def balancesheet(scode,start_date,end_date):
    df = pro.balancesheet(ts_code=scode, start_date=start_date, end_date=end_date,
                          fields='ts_code,ann_date,f_ann_date,end_date,report_type,comp_type,total_share,cap_rese,undistr_porfit,surplus_rese,special_rese,money_cap,'+
'trad_asset,notes_receiv,accounts_receiv,oth_receiv,prepayment,div_receiv,int_receiv,total_cur_assets,time_deposits,oth_assets,fix_assets,r_and_d,cash_reser_cb,indep_acct_assets,total_assets,lt_borr,st_borr,estimated_liab,acc_receivable,payables')
    client.write("/home/hadoop/hive/data/tushare.db/balancesheet/" + scode + ".csv",
                 df.to_csv(header=False, index=False, sep=","), encoding='utf-8', overwrite=True)
#现金流量表
def cashflow(scode,start_date,end_date):
    df = pro.cashflow(ts_code=scode,fields='ts_code,ann_date,end_date,comp_type,report_type,net_profit,finan_exp,free_cashflow', start_date=start_date, end_date=end_date)

    client.write("/home/hadoop/hive/data/tushare.db/cashflow/" + scode + ".csv",
                 df.to_csv(header=False, index=False, sep=","), encoding='utf-8', overwrite=True)


#财务批露日期
def disclosure_date():
    # df = pro.disclosure_date(end_date='20191231')
    df = pro.disclosure_date(ts_code='002475.SZ')
    mongo = MongoBase('disclosureDate')

    mongo.collection.insert(json.loads(df.T.to_json()).values())
    mongo.closeDB()

#主营业务构成
def fina_mainbz():
    df = pro.fina_mainbz(ts_code='002475.SZ', type='P')
    print(df.head(10))

#财务指标数据
def fina_indicator():
    df = pro.fina_indicator(ts_code='002475.SZ')

#港资流向
def moneyflow_hsgt():
    df = pro.moneyflow_hsgt(start_date='20191118', end_date='20191126')
    print(df.head(10))
#沪深十大成交
def hsgt_top10():
    df = pro.hsgt_top10(trade_date='20191125', market_type='1')
    print(df.head(10))

if __name__ == "__main__":
    #get_profit_data()
    # SSE 上交所  SZSE 深交所
    # stock_compay('SSE')
    # stock_compay('SZSE')
    # forecast()
    # income('SSE',1,'20180101','20191111')
    # income('SZSE', 1, '20180101', '20191111')
    # balancesheet('002475.SZ', '20190101', '20191030')
    # cashflow('002475.SZ', '20190101', '20191030')
    # fina_mainbz()

    # disclosure_date()
    moneyflow_hsgt()
    # hsgt_top10()