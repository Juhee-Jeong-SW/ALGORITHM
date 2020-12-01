#-*- encoding: utf-8 -*-
"""수 정렬하기3"""
import sys

N = int(sys.stdin.readline())
answer = [0] * 10001

for _ in range(N):
    index = int(sys.stdin.readline())
    answer[index] = answer[index] + 1 # 인덱스로 입력받고 그 인덱스에는 1 더해서 저장, 숫자 맞춰주기

for i in range(10001):
    if answer[i] != 0:
        for j in range(answer[i]):
            print(i)