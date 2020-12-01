#-*- encoding: utf-8 -*-
"""수 정렬하기2"""

N = int(input())
answer = []

for _ in range(N):
    answer.append(int(input()))

answer = sorted(answer)

for i in answer:
    print(i)
