#-*- encoding: utf-8 -*-
"""피보나치 수 2"""
# 재귀를 이용하면 처음부터 다시 해줘야 하므로, 값을 쌓아갈 수 있도록 반복문과 리스트를 활용한다.

import sys

fib = [0, 1]
n = int(sys.stdin.readline())

for i in range(2, n+1):
    fib.append(fib[i-1]+fib[i-2])

print(fib[-1])