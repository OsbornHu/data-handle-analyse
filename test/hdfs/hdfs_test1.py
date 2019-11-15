import hdfs as hdfs
import tushare as ts
# 错误信息： Permission denied  解决办法 hadoop fs -chmod 777
client=hdfs.Client("http://10.108.1.60:50070",timeout=30000)  #连接到HDFS服务
client.status("/")  #获取指定路径的具体信息
print(client.list("/"))    #获取指定路径的子目录信息
client.makedirs("/test06")   #创建目录

df = ts.get_realtime_quotes('002905')
client.delete("/home/hadoop/hive/data/tushare.db/test.csv")
# client.upload("/test06","/temp/test/transer_mysql.csv")
# client.write("/test06/002905.csv", df.to_csv(header=False,index=False,sep="\t"), encoding='utf-8',overwrite=True)


#client.rename("/test","/new_name")   #重命名
#client.delete("/new_name")  #删除
#client.upload("/test","/opt/bigdata/hadoop/NOTICE.txt")  #上传文件
#client.download("/test/NOTICE.txt","/home")  #下载文件
#client.read("/test/NOTICE.txt")  #读取文件