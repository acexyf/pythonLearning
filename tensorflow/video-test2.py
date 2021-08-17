import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models

# 数据
# https://storage.googleapis.com/laurencemoroney-blog.appspot.com/rps.zip
# https://storage.googleapis.com/laurencemoroney-blog.appspot.com/rps-test-set.zip


model = keras.models.Sequential([
  # 64个滤波器
  keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(28,28,1)),
  # 最大池化
  keras.layers.MaxPool2D(2,2),
  keras.layers.Conv2D(64, (3,3), activation='relu'),
  keras.layers.MaxPool2D(2,2),
  keras.layers.Flatten(),
  keras.layers.Dense(128, activation=tf.nn.relu),
  keras.layers.Dense(10, activation=tf.nn.softmax)
])

print(model, 'model')
