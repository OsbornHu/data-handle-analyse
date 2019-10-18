# -*- encoding=utf-8 -*-

import hdfs
from hdfs import InsecureClient

# 数据框写到hdfs文件
def dataframe_write_to_hdfs(client, hdfs_path, dataframe):
    """
    :param client:
    :param hdfs_path:
    :param dataframe:
    :return:
    """
    client.write(hdfs_path, dataframe.to_csv(header=False,index=False,sep="\t"), encoding='utf-8',overwrite=True)
