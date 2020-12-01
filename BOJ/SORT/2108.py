#-*- encoding: utf-8 -*-
"""통계학"""
import sys
from collections import Counter

# 평균
def average(answer):
    return round(sum(answer) / N)

# 중앙값
def median(answer):
    if N == 1:
        return answer[0]
    else:
        if N % 2 != 0: # 홀수면
            return answer[N//2]
        else : # 짝수면 가운데 두 개 값 더해서 나누기
            return round((answer[N//2+1] + answer[N//2])/2)


# 최빈값
def mode(answer):
    if N == 1 : return answer[0]

    com = Counter(answer).most_common(2)
    if com[0][1] == com[1][1] :
        return com[1][0]
    else:
        return com[0][0]


# 범위
def diff(answer):
    return answer[N-1] - answer[0]


N = int(sys.stdin.readline())
answer = []

for _ in range(N):
    answer.append(int(sys.stdin.readline()))

answer = sorted(answer)

print(average(answer))
print(median(answer))
print(mode(answer))
print(diff(answer))