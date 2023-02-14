# -*- coding: utf-8 -*- 
# @Time : 2022/3/14 21:08 
# @Author : Administrator 
# @Email : o65790uu@qq.com 
# @File : fast_text_.py 
import os
import sys
import jieba


# id_to_label = {}
# idx = 0
# with open('../data1/class.txt', 'r', encoding='utf-8') as f1:
#     for line in f1.readlines():
#         line = line.strip('\n').strip()
#         id_to_label[idx] = line
#         idx += 1
#
# count = 0
# train_data = []
# with open('../data1/dev.txt', 'r', encoding='utf-8') as f2:
#     for line in f2.readlines()[1:]:
#         line = line.strip('\n').strip()
#         sentence, label = line.split('\t')
#         label_id = int(label)
#         label_name = id_to_label[label_id]
#         new_label = '__label__' + label_name
#         sent_char = ' '.join(list(sentence))
#
#         new_sentence = new_label + ' ' + sent_char
#         train_data.append(new_sentence)
#
#         count += 1
#         if count % 10000 == 0:
#             print(count)
#
# with open('../data1/dev_fast.txt', 'w', encoding='utf-8') as f3:
#     for data in train_data:
#         f3.write(data + '\n')

import fasttext

train_data_path = '../data1/train_fast.txt'
test_data_path = '../data1/test_fast.txt'

model = fasttext.train_supervised(input=train_data_path, wordNgrams=2)

res = model.test(test_data_path)
print(res)

# import time
# train_data_path = '../data1/train_fast.txt'
# dev_data_path = '../data1/dev_fast.txt'
# test_data_path = '../data1/test_fast.txt'
#
# model = fasttext.train_supervised(input=train_data_path,
#                                   autotuneValidationFile=dev_data_path,
#                                   autotuneDuration=600,
#                                   wordNgrams=2,
#                                   verbose=3)
#
# # 在测试集上评估模型的表现
# result = model.test(test_data_path)
# print(result)
#
# # 模型保存
# time1 = int(time.time())
# model_save_path = "./toutiao_fasttext_{}.bin".format(time1)
# model.save_model(model_save_path)





