#-*- encoding: utf-8 -*-
"""스타트와 링크"""
#참고 : https://juhee-maeng.tistory.com/60

import sys
from itertools import combinations
from collections import deque


def ability(team, S):
    n = len(team)
    sumNum = 0

    for x in range(0, n-1):
        for y in range(x+1, n):
            sumNum += S[team[x]][team[y]] + S[team[y]][team[x]]

    return sumNum


N = int(input()) ## 총 몇명?
S = [list(map(int, input().split())) for _ in range(N)] ## 능력에대한 정보
A = [int(i) for i in range(N)] ## 각 선수에게 0부터 N-1까지 숫자 부여
team = deque(combinations(A, N//2))
minNum = sys.maxsize ##업데이트 해야 될 값.

start_team = deque()
link_team = deque()

for _ in range(len(team)//2):
    start_team.append(team.popleft())
    link_team.append(team.pop())

for i in range(len(start_team)):
    answer = abs(ability(start_team[i], S) - ability(link_team[i], S))

    if answer < minNum:
        minNum = answer

print(minNum)