#-*- encoding: utf-8 -*-
"""단어 공부"""
from collections import Counter

text = str(input())
text = Counter(text.upper())
count_list = list(text.values())

max_value = max(count_list)
temp = count_list.count(max_value)


if temp >= 2 :
    print('?')
else :
    for k, v in text.items():
        if v == max_value :
            print(k)

