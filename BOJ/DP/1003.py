#-*- encoding: utf-8 -*-
"""피보나치 함수"""
#idea : 재귀함수를 이용하면 시간 초과가 나므로, 점화식을 이용하여 풀이한다.
#0부터 시작할 떄와 1부터 시작하는 것이 독립적으로 움직임으로 나눠서 해줌.

import sys

#낚시용
def fibonacci(n):
    global cnt0
    global cnt1
    if n == 0:
        cnt0 += 1
        return 0
    elif n == 1:
        cnt1 += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


answer = []
T = int(sys.stdin.readline())
fibo0 = [0 for _ in range(41)]
fibo1 = [0 for _ in range(41)]

fibo0[0] = 1
fibo1[1] = 1

for _ in range(T):
    N = int(sys.stdin.readline())
    for i in range(2, N+1):
        fibo0[i] = fibo0[i-1] + fibo0[i-2]
    for i in range(2, N+1):
        fibo1[i] = fibo1[i-1] + fibo1[i-2]

    answer.append((fibo0[N], fibo1[N]))


for i in answer:
    print(i[0], i[1])