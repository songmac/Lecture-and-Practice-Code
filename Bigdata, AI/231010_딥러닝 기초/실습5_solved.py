## 실습5. base line 모델을 먼저 만들고, 성능(acc 90%이상)향상 모델을 만들어보세요! (solved)

# 데이터명 : 타이타닉 생존자
# 데이터 샘플수 : 891개
# 필드수 : 15개

# <머신러닝 모델을 만들 때의 순서>
# 1. 데이터 셋의 특징을 잘 나타낼 수 있게 전처리를 한다. (input shape = 14개)
# 2. 학습이 제대로 되도록 데이터 셋을 잘 쪼갠다. (Train, Validation, Test)
# 3. 목적과 데이터에 맞는 모델을 생성한다. (overfitting 방지용 dropout)
# (추가로, 사용하면 좋은 메트릭스 precision, recall, or F1-score )
# 4. 학습 후 모델의 성능을 평가하고, 성능을 업그레이드한다.

import pandas as pd
import numpy as np
import tensorflow as tf
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# 데이터셋 로드
titanic = sns.load_dataset("titanic")

# 결측치 제거
titanic = titanic.dropna()

# feature과 label 설정
X = titanic[['pclass', 'sex', 'age', 'fare', 'sibsp', 'parch', 'class', 'embarked']]
y = titanic['survived']

# 숫자가 아닌 'sex' 열 값 인코딩
X['sex'] = LabelEncoder().fit_transform(X['sex'])

#  2개 이상의 분류 값을 가진 'class'와 'embarked'열 one-hot 인코딩 수행
X = pd.get_dummies(X, columns=['class', 'embarked'], drop_first=True)

# 데이터셋 학습, 검증 용으로 분류
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 정의 및 컴파일
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 모델 학습시키기
history = model.fit(X_train, y_train, validation_data=(X_valid, y_valid), epochs=1000, batch_size=32)

# 모델 평가하기
accuracy = model.evaluate(X_valid, y_valid)[1]
print(f"Validation Accuracy: {accuracy * 100:.2f}%")  