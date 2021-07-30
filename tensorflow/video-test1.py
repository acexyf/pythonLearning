import tensorflow as tf
from tensorflow import keras

fashion_mnist = keras.datasets.fashion_mnist


(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


model = keras.Sequential([
  keras.layers.Flatten(input_shape=(28, 28)),
  keras.layers.Dense(128, activation=tf.nn.relu),
  keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer=keras.optimizers.Adam(), loss='sparse_categorical_crossentropy')


model.fit(train_images,train_labels, epochs=5)

loss_and_metrics = model.evaluate(test_images,test_labels)

classifications = model.predict(test_images)

print(loss_and_metrics)
print(classifications[0])
print(test_labels[0])