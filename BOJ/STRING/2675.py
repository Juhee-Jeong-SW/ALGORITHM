#-*- encoding: utf-8 -*-
"""문자열 반복"""

case_size = int(input())
strings = []
answer = []

for _ in range(case_size) :
    strings.append(input().split(' '))

for i in range(case_size) :
    for j in range(len(strings[i][1])) :
        answer.append(strings[i][1][j] * int(strings[i][0]))
    print(''.join(answer))
    answer = []
