#-*- encoding: utf-8 -*-
"""ACM 호텔"""
#idea : 층은 n에서 층을 나눈 나머지 이용하고, 방 번호는 n에서 층을 나눈 몫에 1을 더한 값을 합쳐서 단지수를 나타낸다.

import sys

T = int(input())
answer = []

for _ in range(T) :
    h, w, n = map(int, sys.stdin.readline().split(' '))

    floor = n % h

    apt = (n//h) + 1

    if floor == 0 :
        floor = h
        apt -= 1

    answer.append(floor*100 + apt)

for i in answer :
    print(i)