from participle import segText, get_stop_words
import numpy as np
from keras.models import load_model
from keras.preprocessing import sequence
import pickle

model = load_model('model.pkl')
tokenizer = pickle.load(open("tokenizer.pkl", 'rb'))
stop = get_stop_words()

def process(text):
    x_text = np.array([segText(text, stop)])
    x_test_seq = tokenizer.texts_to_sequences(x_text)
    x_train = sequence.pad_sequences(x_test_seq, maxlen=50)
    return model.predict_classes(x_train)

