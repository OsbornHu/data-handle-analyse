import hdfs as hdfs


client=hdfs.Client("http://10.108.1.56:50070")  #连接到HDFS服务
client.status("/")  #获取指定路径的具体信息
print(client.list("/"))    #获取指定路径的子目录信息
client.makedirs("test06")   #创建目录
client.rename("/test","/new_name")   #重命名
client.delete("/new_name")  #删除
client.upload("/test","/opt/bigdata/hadoop/NOTICE.txt")  #上传文件
client.download("/test/NOTICE.txt","/home")  #下载文件
client.read("/test/NOTICE.txt")  #读取文件