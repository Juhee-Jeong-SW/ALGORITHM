#-*- encoding: utf-8 -*-
"""그룹 단어 체커"""
import sys

size = int(input())
strings = []
sum = 0

for _ in range(size) :
    strings.append(str(input()))

for i in strings :
    for j in range(len(i)) :
        if j != len(i) - 1 :
            if i[j] == i[j+1] :
                pass
            elif i[j] in i[j+1:] :
                break
        else:
            sum += 1

print(sum)
#print(strings)

