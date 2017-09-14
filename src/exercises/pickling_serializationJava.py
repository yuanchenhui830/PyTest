#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle
d = dict(name='Bob', age=20, score=88)
b = pickle.dumps(d)
with open('C:/Users/YCH/Desktop/txt.txt', 'wb') as fw:
    fw.write(b)

"""或者"""
with open('C:/Users/YCH/Desktop/txt.txt', 'wb') as fw:
    pickle.dump(d,fw)

with open('C:/Users/YCH/Desktop/txt.txt', 'rb') as fr:
    d = pickle.load(fr)
print(d)
