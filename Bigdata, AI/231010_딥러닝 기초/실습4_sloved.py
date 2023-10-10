## 실습4. base line 모델을 먼저 만들고, 성능(acc 90%이상)향상 모델을 만들어보세요!

# 데이터명 : IRSI (붓꽃 데이터)
#  데이터설명 : 붓꽃 데이터로, 꽃잎의 각 부분의 너비와 길이등을 측정한 데이터
#  샘플수 : 150개
#  필드수 : 5개

# - sepal_length 꽃받침 길이
# - sepal_width 꽃받침 너비
# - petal_length 꽃잎 길이
# - petal_width 꽃잎 너비
# - species 꽃 종류(setosa, versicolor, virginica)

import tensorflow as tf
import tensorflow_datasets as tfds
import pandas as pd
import numpy as np

import seaborn as sns
iris = sns.load_dataset("iris")
iris

train_dataset = tfds.load('iris', split='train[:80%]')
valid_dataset = tfds.load('iris', split='train[80%:]')

def preprocess(data):
    # 코드를 입력하세요
    x = data['features']
    y = data['label']
    y = tf.one_hot(y, 3)
    return x, y

batch_size=10
train_data = train_dataset.map(preprocess).batch(batch_size)
valid_data = valid_dataset.map(preprocess).batch(batch_size)

model = tf.keras.models.Sequential([
    # input_shape는 X의 feature 갯수가 4개 이므로 (4, )로 지정합니다.
    tf.keras.layers.Dense(512, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    # Classification을 위한 Softmax, 클래스 갯수 = 3개
    tf.keras.layers.Dense(3, activation='softmax'),
])

model.summary()

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])

history = model.fit(train_data,
                    validation_data=(valid_data),
                    epochs=20)

import matplotlib.pyplot as plt
plt.figure(figsize=(12, 9))
plt.plot(np.arange(1, 21), history.history['loss'])
plt.plot(np.arange(1, 21), history.history['val_loss'])
plt.title('Loss / Val Loss', fontsize=20)
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend(['loss', 'val_loss'], fontsize=15)
plt.show()

plt.figure(figsize=(12, 9))
plt.plot(np.arange(1, 21), history.history['acc'])
plt.plot(np.arange(1, 21), history.history['val_acc'])
plt.title('Acc / Val Acc', fontsize=20)
plt.xlabel('Epochs')
plt.ylabel('Acc')
plt.legend(['acc', 'val_acc'], fontsize=15)
plt.show()

