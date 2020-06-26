
from sklearn.model_selection import train_test_split

import numpy as np

pos_data = np.load('pos.npy')
neg_data = np.load('neg.npy')

all_labels = np.append((np.ones(len(pos_data))), (np.zeros(len(neg_data))), axis=0)
all_texts = np.append(pos_data, neg_data, axis=0)

x_train, x_test, y_train, y_test = train_test_split(all_texts, all_labels, test_size=0.1)


def save_data(doc_path, data):
    np.save(doc_path, data)





save_data('./data/x_train_data.npy', x_train)
save_data('./data/x_test_data.npy', x_test)
save_data('./data/y_train_data.npy', y_train)
save_data('./data/y_test_data.npy', y_test)
