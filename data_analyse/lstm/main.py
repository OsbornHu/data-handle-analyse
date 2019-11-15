import tensorflow
import data_analyse.lstm.download as download
import data_analyse.lstm.merge as merge
import data_analyse.lstm.chose as chose
import data_analyse.lstm.LSTM as LSTM

market = ["a"]
time = "201601"
start_time = "20160101"

for i in range(len(market)):
   download.download(time,start_time,market[i])
   merge.merge(time,market[i])
   chose.chose(time,market[i])

for i in range(len(market)):
    LSTM.two_up(time,market[i])
