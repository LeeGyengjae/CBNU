import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist

# 1. MNIST 데이터셋 로드
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 2. 데이터 전처리
# 픽셀 값을 0~1 사이로 정규화
x_train = x_train / 255.0
x_test = x_test / 255.0

# 정답 레이블(클래스)을 원-핫 인코딩
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# 3. MLP 모델 정의
model = Sequential([
    Flatten(input_shape=(28, 28)),  # 데이터를 1차원 벡터로 평탄화
    Dense(128, activation='relu'),  # 첫 번째 은닉층
    Dense(64, activation='relu'),  # 두 번째 은닉층
    Dense(10, activation='softmax')  # 출력층 (10개의 클래스)
])

# 4. 모델 컴파일
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 5. 모델 학습
model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# 6. 모델 평가
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"테스트 정확도: {test_accuracy * 100:.2f}%")