#-*- encoding: utf-8 -*-
"""Fly me to the Alpha Centauri"""
#idea : 규칙 거리가 N의 제곱 or N의 제곱 + N의 거리 이후 횟수가 증가한다.
# N의 제곱일 때 횟수는 (2 * N) - 1 / N의 제곱 + N 이하는 2 * N / 그 이후는 (2 * N) + 1

#참고 : https://wlstyql.tistory.com/54


import sys
import math

T = int(sys.stdin.readline())
for _ in range(T):

    x, y = map(int, sys.stdin.readline().split())
    diff = int(y - x)

    if diff <= 3:
        print(diff)

    else:
        n = int(math.sqrt(diff))

        if diff == n ** 2:
            print(2*n-1)

        elif n ** 2 < diff <= n ** 2 + n:
            print(2*n)

        else:
            print(2*n+1)


"""첫번째 실패 코드
T = int(sys.stdin.readline())
answer = []

for _ in range(T) :
    x, y = map(int, sys.stdin.readline().split(' '))
    diff = (y - 1) - (x + 1)
    count = 2
    count1 = 0
    count2 = 0
    
    if diff >= 2 :
        count1 = diff // 2
        count2 = diff % 2
    else :
        count += diff
    
    count += (count1 + count2)
    
    answer.append(count)
    
    for i in answer :
        print(i)"""

