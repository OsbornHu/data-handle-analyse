https://blog.csdn.net/yujuan110/article/details/78457259

(1)初始化，输入命令，bin/hdfs namenode -format 
(2)全部启动sbin/start-all.sh，也可以分开sbin/start-dfs.sh、sbin/start-yarn.sh 
(3)终止服务器：sbin/stop-all.sh 
(4)输入命令jps，可以看到相关信息


(2)浏览器打开http://10.108.1.60:8088/ 
(3)浏览器打开http://10.108.1.60:50070/ 





nohup hive --service metastore  >/dev/null &

nohup hiveserver2 >/dev/null &



