## 실습 3 - 텐서플로우로 로지스틱회귀 모델링

# x = np.array([2,4,6,8,10])
# y = np.array([0,0,0,1,1])

# 로지스틱회귀모델을 만들고 ‘9’을 넣었을때 값을 예측해보세요.

import numpy as np
import tensorflow as tf
import keras


x_train = np.array([2,4,6,8,10])
y_train = np.array([0,0,0,1,1])

model = tf.keras.models.Sequential() #모델선언

model.add(tf.keras.layers.Dense(1, input_dim = 1, activation = 'sigmoid')) #1차원 #선형회귀

model.summary()

sgd = tf.keras.optimizers.SGD(learning_rate=0.01)

model.compile(loss = 'binary_crossentropy', optimizer = 'sgd', metrics = ['accuracy'])
model.fit(x_train, y_train, epochs = 1, batch_size = 1)

model.predict([9]) #2차원 리스트로 묶어서 넣어주기
