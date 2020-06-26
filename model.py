from keras.layers.embeddings import Embedding
from keras.layers.core import Dense
from keras.layers.convolutional import Conv1D
from keras.layers.core import Dropout, Flatten
from keras.layers.pooling import MaxPooling1D
from keras.layers.recurrent import GRU
from keras.models import Sequential
import numpy as np
import tensorflow as tf
from keras import backend as K
from keras.models import load_model

x_train = np.load('x_train.npy')
y_train = np.load('./data/y_train_data.npy')
x_test = np.load('x_test.npy')
y_test = np.load('./data/y_test_data.npy')

# TextCNN-GRU
# model = Sequential()
# model.add(Embedding(2000, 64, input_length=50))
# model.add(Conv1D(filters=64, kernel_size=4, padding='same', activation='relu'))
# model.add(MaxPooling1D(pool_size=2))
# model.add(Dropout(0.25))
# model.add(Conv1D(filters=64, kernel_size=4, padding='same', activation='relu'))
# model.add(MaxPooling1D(pool_size=2))
# model.add(Dropout(0.25))
# model.add(GRU(64, activation='relu'))
# model.add(Dropout(0.25))
# model.add(Dense(64, activation='relu'))
# model.add(Dense(32, activation='relu'))
# model.add(Dense(1, activation='sigmoid'))

# TextCNN
# model = Sequential()
# model.add(Embedding(2000, 64, input_length=50))
# model.add(Conv1D(filters=64, kernel_size=4, padding='same', activation='relu'))
# model.add(MaxPooling1D(pool_size=2))
# model.add(Dropout(0.25))
# model.add(Flatten())
# model.add(Dense(64, activation='relu'))
# model.add(Dense(32, activation='relu'))
# model.add(Dense(1, activation='sigmoid'))

# GRU
model = Sequential()
model.add(Embedding(2000, 64, input_length=50))
model.add(GRU(64, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

def auc(y_true, y_pred):
    auc = tf.metrics.auc(y_true, y_pred)[1]
    K.get_session().run(tf.local_variables_initializer())
    return auc

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=[auc])
#
model.fit(x_train, y_train, epochs=5, batch_size=128)
# model.save('gru_model.h5')

# model = load_model('gru_model.h5')
# score = model.evaluate(x_test, y_test)
# print(score)



scores = model.evaluate(x_test, y_test)

print(scores)
