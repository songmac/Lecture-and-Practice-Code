## 실습5. base line 모델을 먼저 만들고, 성능(acc 90%이상)향상 모델을 만들어보세요!

# 데이터명 : 타이타닉 생존자
# 데이터 샘플수 : 891개
# 필드수 : 15개


# <머신러닝 모델을 만들 때의 순서>
# 1. 데이터 셋의 특징을 잘 나타낼 수 있게 전처리를 한다.
# 2. 학습이 제대로 되도록 데이터 셋을 잘 쪼갠다. (Train, Validation, Test)
# 3. 목적과 데이터에 맞는 모델을 생성한다.
# 4. 학습 후 모델의 성능을 평가하고, 성능을 업그레이드한다.


import tensorflow as tf
import tensorflow_datasets as tfds
import pandas as pd
import numpy as np

import seaborn as sns
titanic = sns.load_dataset("titanic")
titanic

train_dataset = tfds.load('titanic', split='train[:80%]')
valid_dataset = tfds.load('titanic', split='train[80%:]')

def preprocess(data):
    # 코드를 입력하세요
    x = data['features']
    y = data['label']
    y = tf.one_hot(y, 3)
    return x, y

batch_size=1
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