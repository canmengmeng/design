from django.shortcuts import render
from django.http import HttpResponse
from keras.models import load_model
import jieba.posseg
import pickle
import numpy as np
from keras.preprocessing import sequence


# Create your views here.
def index(request):
    return render(request, 'index.html')



def analysis_action(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        stop = [line.strip() for line in open(r'E:\PycharmCode\Graduation_Design\stopwords.txt', encoding='UTF-8').readlines()]
        tokenizer = pickle.load(open(r"E:\PycharmCode\Graduation_Design\tokenizer.pkl", 'rb'))
        model = load_model(r"E:\PycharmCode\Graduation_Design\gru_model.h5")
        cutText = jieba.posseg.cut(text)
        resText = []
        for word, flag in cutText:
            if flag == 'nr' or flag == 'ns' or flag == 'nt' or flag == 'nz':
                pass
            else:
                if word not in stop and word != ' ':
                    resText.append(word)
        segText = " ".join(resText)
        x_text = np.array([segText])
        x_test_seq = tokenizer.texts_to_sequences(x_text)
        x_train = sequence.pad_sequences(x_test_seq, maxlen=50)
        res = model.predict_classes(x_train)[0][0]
        return HttpResponse(str(res))


# print(str(test.process('总的来说，有点乱七八糟的感觉，而且纸质差')[0][0]))
