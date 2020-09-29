#-*- encoding: utf-8 -*-
"""토마토"""
# idea : 기존의 bfs를 적용하나 방문했던 visited 배열을 없애고, 방문할 때마다 일수를 증가시키는 것으로 확인한다.
# 그 중 리스트에서 가장 큰 수를 찾으면 최소 일수가 된다.
# 마지막에 다 익은 경우와 익을 수 없는 경우는 flag와 result 변수를 이용하여 구분해주었다.
# queue를 리스트로 선언할 경우 , 첫번째 원소를 반환하고 모든 원소를 한 칸씩 이동해야 하므로 O(n)만큼 시간이 더 걸려서 ->시간 초과임.
import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
matrix = [list(map(int,input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque() # bfs를 활용하기 위한 queue
result = -2

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft() # queue에 들어있던 이미 방문한 지점에 대해 x,y로 가져온다.
    for i in range(4): # dfs 와 동일하게 진행함. 주변 x,y탐색하는 법
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if matrix[nx][ny] == 0:
                # 방문한 적이 없고, 인접한 곳일 경우(미로의 한 방향일 경우) 방문한다.
            matrix[nx][ny] = matrix[x][y] + 1 # 이동했으므로 거리에 1을 더해준다.
            queue.append((nx,ny)) # 방문했으므로 queue에 등록한다.

flag = False

for i in matrix:
    for j in i:
        if j == 0:
            flag = True
        result = max(result, j)

if flag: # 못 익은 게 있으면
    print(-1)
elif result == -2: # 기존에 다 익어있으면
    print(0)
else : # 결과값 구하기
    print(result-1)