#-*- encoding: utf-8 -*-
"""벌집"""

#idea : 육각형이라는 성질을 이용하여 각 층마다 6개씩 증가함을 나타내는 식을 세워 만족할 경우 멈춘다.
#첫번째 시도 -> 시간 초과 (답도 틀림) 방정식 이용하여 구하려 함( n <= 1 + (x * 6)
#두번째 시도 -> 문제를 다시 잘 읽고 식을 재정립하였다. 마지막 숫자는 계속해서 6 곱한 것과 이전 합들의 합이다.


import sys
n = int(sys.stdin.readline())
count = 1
sum = 1

if n == 1 :
    print(1)

else :
    while True :
        sum += (count * 6)
        if n <= sum :
            print(count + 1)
            break
        else :
            count += 1
