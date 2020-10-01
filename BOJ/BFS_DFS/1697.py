#-*- encoding: utf-8 -*-
"""숨바꼭질"""
#idea : 모든 가지수를 다 파악하도록 bfs를 이용한다. 총 v-1, v+1, v*2에 해당하는 가지수를 방문해서 K를 만날 때 종료시킨다.

import sys
from collections import deque


def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        v = queue.popleft()
        if v == K:
            return visited[v]
        for i in (v-1, v+1, v*2):
            if 0 <= i < MAX and not visited[i]: # 범위 안에 있으면서 아직 방문한 노드가 아닐 때
                visited[i] = visited[v] + 1 # 방문한 곳에 시간을 1 더해주고
                queue.append(i) # 방문한 노드를 큐에 삽입


MAX = 100001
N, K = map(int, sys.stdin.readline().split())
visited = [0] * MAX
print(bfs(N))