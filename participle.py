import pandas as pd
import numpy as np
import jieba
import jieba.posseg


def get_data():
    pos_data = pd.read_csv("JDview/JDview/spiders/pos.csv", encoding='utf-8', sep=None, engine='python', usecols=[0])
    neg_data = pd.read_csv("JDview/JDview/spiders/neg.csv", encoding='utf-8', sep=None, engine='python', usecols=[0])

    return pos_data, neg_data


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


def start_neg(neg_data):
    neg_List = []
    for index, row in neg_data.iterrows():
        content = row[0]
        if len(content) < 100:
            print(index)
            segContent = segText(content)
            if len(segContent) > 0:
                neg_List.append(segContent)
    npText = np.array(neg_List)
    np.save("neg.npy", npText)

def start_pos(pos_data):
    pos_List = []
    for index, row in pos_data.iterrows():
        content = row[0]
        if len(content) < 100:
            print(index)
            segContent = segText(content)
            if len(segContent) > 0:
                pos_List.append(segContent)
    npText = np.array(pos_List)
    np.save("pos.npy", npText)

