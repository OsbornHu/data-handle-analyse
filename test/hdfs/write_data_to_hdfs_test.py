import hdfs as hdfs


client=hdfs.Client("http://10.108.1.60:50070")  #连接到HDFS服务

reader = client.read("/user/hive/warehouse/test.db/flight_info")  #读取文件

