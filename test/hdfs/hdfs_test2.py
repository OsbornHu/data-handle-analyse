from hdfs import InsecureClient
client = InsecureClient("http://10.108.1.56:50070",user='hive')
print(client.list("/"))