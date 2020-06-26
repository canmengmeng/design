from keras.models import load_model
import pickle
import numpy as np
import jieba.posseg
from keras.preprocessing import sequence


def get_stop_words():
    stopwords = [line.strip() for line in open('stopwords.txt', encoding='UTF-8').readlines()]
    return stopwords

def segText(text, stopwords):
    cutText = jieba.posseg.cut(text)
    resText = []
    for word, flag in cutText:
        if flag == 'nr' or flag == 'ns' or flag == 'nt' or flag == 'nz':
            pass
        else:
            if word not in stopwords and word != ' ':
                resText.append(word)
    return " ".join(resText)

def process(text):
    model = load_model('model.pkl')
    tokenizer = pickle.load(open("tokenizer.pkl", 'rb'))
    stop = get_stop_words()
    x_text = np.array([segText(text, stop)])
    x_test_seq = tokenizer.texts_to_sequences(x_text)
    x_train = sequence.pad_sequences(x_test_seq, maxlen=50)
    return model.predict_classes(x_train)

print(process('总的来说，有点乱七八糟的感觉，而且纸质差'))
