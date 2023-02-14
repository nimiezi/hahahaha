# -*- coding: utf-8 -*- 
# @Time : 2022/3/14 21:56 
# @Author : Administrator 
# @Email : o65790uu@qq.com 
# @File : test.py 
import requests
import time

# 定义请求url和传入的data
url = "http://0.0.0.0:5000/v1/main_server/"
data = {"uid": "AI-6-202104", "text": "公共英语(PETS)写作中常见的逻辑词汇汇总"}

start_time = time.time()
# 向服务发送post请求
res = requests.post(url, data=data)

cost_time = time.time() - start_time

# 打印返回的结果
print('输入文本:', data['text'])
print('分类结果:', res.text)
print('单条样本预测耗时: ', cost_time * 1000, 'ms')

