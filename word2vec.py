from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
import pickle

import numpy as np

train_data = np.load('./data/x_train_data.npy')
test_data = np.load('./data/x_test_data.npy')

tokenizer = Tokenizer(num_words=2000)
tokenizer.fit_on_texts(train_data)

x_train_seq = tokenizer.texts_to_sequences(train_data)
x_test_seq = tokenizer.texts_to_sequences(test_data)

x_train = sequence.pad_sequences(x_train_seq, maxlen=50)
x_test = sequence.pad_sequences(x_test_seq, maxlen=50)

np.save('./x_train.npy', x_train)
np.save('./x_test.npy', x_test)
