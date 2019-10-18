import datetime

# 自定义获取昨天日期的函数
def getYesterday():
    """
    :return: 获取昨天日期
    """
    today = datetime.date.today()
    oneday=datetime.timedelta(days=1)
    yesterday=today-oneday
    # 日期转字符串
    partition_date=yesterday.strftime('%Y-%m-%d')
    return partition_date