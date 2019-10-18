import tushare as ts
import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import preprocessing


#readdata=ts.get_hist_data('002905')
#readdata.to_csv('/temp/inbox/000725.csv')
data = pd.read_csv('/temp/inbox/000725.csv')
#data = pd.DataFrame(readdata)

##print(data.info())

#data.drop(columns=['date', 'ma5', 'ma10', 'ma20', 'v_ma5', 'v_ma10', 'v_ma20'], axis=1, inplace=True)
print(data.head())
#print(data['close'])


##plt.plot(data['close'])
##plt.show()

##data2 = ts.get_today_all()
##print(data2)

data_train = data.iloc[:int(data.shape[0] * 0.8), :]  #训练集
data_test = data.iloc[int(data.shape[0] * 0.8):, :]   #测试集

##数据归一化
scaler = preprocessing.MinMaxScaler(feature_range=(-1, 1))
scaler.fit(data_train)
#scaler.fit(data_test)
data_train = scaler.transform(data_train)
data_test = scaler.transform(data_test)

##设置X 与 Y
X_train = data_train[:, 0:3]
y_train = data_train[:, 4]
X_test = data_test[:, 0:3]
y_test = data_test[:, 4]

##设置超参数
input_dim = X_train.shape[1]
output_dim = 1
hidden_1 = 1024
hidden_2 = 512
hidden_3 = 256
hidden_4 = 128
batch_size = 256
epochs = 10

##设置占位符
X = tf.placeholder(shape=[None, input_dim], dtype=tf.float32)
Y = tf.placeholder(shape=[None], dtype=tf.float32)

##设置神经网络
## 第一层
W1 = tf.get_variable('W1', [input_dim, hidden_1], initializer=tf.contrib.layers.xavier_initializer(seed=1))
b1 = tf.get_variable('b1', [hidden_1], initializer=tf.zeros_initializer())
## 第二层
W2 = tf.get_variable('W2', [hidden_1, hidden_2], initializer=tf.contrib.layers.xavier_initializer(seed=1))
b2 = tf.get_variable('b2', [hidden_2], initializer=tf.zeros_initializer())
## 第三层
W3 = tf.get_variable('W3', [hidden_2, hidden_3], initializer=tf.contrib.layers.xavier_initializer(seed=1))
b3 = tf.get_variable('b3', [hidden_3], initializer=tf.zeros_initializer())
## 第四层
W4 = tf.get_variable('W4', [hidden_3, hidden_4], initializer=tf.contrib.layers.xavier_initializer(seed=1))
b4 = tf.get_variable('b4', [hidden_4], initializer=tf.zeros_initializer())
## 输出层
W5 = tf.get_variable('W5', [hidden_4, output_dim], initializer=tf.contrib.layers.xavier_initializer(seed=1))
b5 = tf.get_variable('b5', [output_dim], initializer=tf.zeros_initializer())

##设置网络结构
h1 = tf.nn.relu(tf.add(tf.matmul(X, W1), b1))
h2 = tf.nn.relu(tf.add(tf.matmul(h1, W2), b2))
h3 = tf.nn.relu(tf.add(tf.matmul(h2, W3), b3))
h4 = tf.nn.relu(tf.add(tf.matmul(h3, W4), b4))
out = tf.transpose(tf.add(tf.matmul(h4, W5), b5))

loss = tf.reduce_mean(tf.squared_difference(out, Y))
optimizer = tf.train.AdamOptimizer().minimize(loss)


##训练
with tf.Session() as sess:
    ## 初始化所有变量
    sess.run(tf.global_variables_initializer())

    for e in range(epochs):
        ## 将数据打乱
        shuffle_indices = np.random.permutation(np.arange(y_train.shape[0]))
        X_train = X_train[shuffle_indices]
        y_train = y_train[shuffle_indices]

        for i in range(y_train.shape[0] // batch_size):
            start = i * batch_size
            batch_x = X_train[start : start + batch_size]
            batch_y = y_train[start : start + batch_size]
            sess.run(optimizer, feed_dict={X: batch_x, Y: batch_y})

            if i % 50 == 0:
                print('MSE Train:', sess.run(loss, feed_dict={X: X_train, Y: y_train}))
                print('MSE Test:', sess.run(loss, feed_dict={X: X_test, Y: y_test}))
                y_pred = sess.run(out, feed_dict={X: X_test})
                y_pred = np.squeeze(y_pred)
                plt.plot(y_test, label='test')
                plt.plot(y_pred, label='pred')
                plt.title('Epoch ' + str(e) + ', Batch ' + str(i))
                plt.legend()
                plt.show()
