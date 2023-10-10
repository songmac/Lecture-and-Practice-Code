# ## 실습 2 - 텐서플로우로 선형회귀 모델링

# x = np.array([[2,0],[4,5],[6,3],[8,5],[10,7]])
# y = np.array([20,24,37,40,50])

# 선형회귀모델을 만들고 ‘[5,7]’를 넣었을때 값을 예측해보세요.


import numpy as np
import tensorflow as tf
import keras

#from tensorflow.keras.models import Sequential
#fom tensorflow.keras.layers import Dense

import numpy as np

x_train = np.array([[2,0],[4,5],[6,3],[8,5],[10,7],[1,0],[3,5],[8,3],[10,5],[19,7]])
y_train = np.array([20,24,37,40,50, 60, 70, 80, 90, 100])

model = tf.keras.models.Sequential() #모델선언

model.add(tf.keras.layers.Dense(1, input_dim = 2, activation = 'linear')) #1차원 #선형회귀
model.add(tf.keras.layers.Dense(1, activation = 'sigmoid'))

model.summary()

sgd = tf.keras.optimizers.SGD(learning_rate=0.08)

model.compile(loss = 'mse', optimizer = 'sgd', metrics = ['accuracy'])
model.fit(x_train, y_train, epochs = 10, batch_size = 1)

model.predict([[5,7]]) #2차원 리스트로 묶어서 넣어주기