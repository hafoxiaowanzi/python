import tensorflow as tf

print(tf.__version__)

mnist = tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test) = mnist.load_data()
print(x_train.shape,y_train.shape)
print(x_test.shape,y_test.shape)

import matplotlib.pyplot as plt

image_index = 1234

plt.imshow(x_train[image_index],cmap='Greys')
plt.show()
print(y_train[image_index])

import numpy as np

x_train = np.pad( x_train, ((0, 0),(2, 2),(2, 2)), 'constant', constant_values = 0 )
print(x_train.shape)

x_train = x_train.astype('float32')

x_train /= 255

x_train = x_train.reshape(x_train.shape[0],32,32,1)

print(x_train.shape)
