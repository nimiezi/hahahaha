# -*- coding: utf-8 -*- 
# @Time : 2022/3/14 20:04 
# @Author : Administrator 
# @Email : o65790uu@qq.com 
# @File : random_forest_.py 
# import pandas as pd
# from collections import Counter
# import numpy as np
# import jieba
# content = pd.read_csv('../data1/train.txt', sep='\t')
# count = Counter(content.label.values)
# print(count)
#
# total = 0
# for i, v in count.items():
#     total += v
# for i, v in count.items():
#     print(i, v / total * 100, '%')
# content['sentence_len'] = content['sentence'].apply(len)
# length_mean = np.mean(content['sentence_len'])
# length_std = np.std(content['sentence_len'])
# print(length_mean, length_std)
#
#
# def cut_sentence(s):
#     return jieba.lcut(s)
# content['words'] = content['sentence'].apply(cut_sentence)
# content['words'] = content['sentence'].apply(lambda s: ' '.join(cut_sentence(s)))
# content['words'] =  content['words'].apply(lambda s: ' '.join(s.split())[:30])
# content.to_csv('../data1/train_new.csv')


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

train_corpus = '../data1/train_new.csv'
stop_words_path = '../data1/stopwords.txt'
content = pd.read_csv(train_corpus)
corpus = content['words'].values
stop_words_size = 749
words_long_tail_begin = 10000
words_size = words_long_tail_begin - stop_words_size
stop_words = open(stop_words_path, encoding='utf-8').read().split()[:stop_words_size]
tfidf = TfidfVectorizer(max_features=words_size, stop_words=stop_words)
text_vectors = tfidf.fit_transform(corpus)
print(text_vectors.shape)

target = content['label']
x_train, x_test,y_train, y_test = train_test_split(text_vectors, target,test_size=0.2)
model = RandomForestClassifier()
model.fit(x_train, y_train)
acc = accuracy_score(model.predict(x_test), y_test)
print(acc)
