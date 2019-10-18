import tushare as ts
import hdfs as hdfs
from common import hdfs_utils
from hdfs import InsecureClient
import time as time
import matplotlib.pyplot as plt

client = InsecureClient("http://10.108.1.56:50070",user='hive')

df = ts.get_hist_data('002905')

# print(client.list("/"))

with client.read("/kylin/", encoding="utf-8", delimiter="\n") as reader:
 for line in reader:
  time.sleep(1)
  print(line)

#hdfs_utils.dataframe_write_to_hdfs(client,"/002905.csv",df)

#client.write("/002905.csv", df.to_csv(header=False,index=False,sep="\t"), encoding='utf-8',overwrite=True)

