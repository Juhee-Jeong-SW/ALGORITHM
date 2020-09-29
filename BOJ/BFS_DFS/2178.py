#-*- encoding: utf-8 -*-
"""미로 탐색"""
# bfs으로 접근하는지 모르고 dfs로 연구하다가 안 돼서 참고했다.
# 참고 : https://chancoding.tistory.com/64

import sys
sys.setrecursionlimit(10 ** 9) # 런타임 에러 해결

N, M = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = [(0,0)] # bfs를 활용하기 위한 queue
visited[0][0] = 1 # 방문 이력 표시 1이면 방문 아니면 0

while queue:
    x, y = queue.pop(0) # queue에 들어있던 이미 방문한 지점에 대해 x,y로 가져온다.

    if x == N-1 and y == M-1: # 가장 마지막 부분 : 도착 부분
        print(visited[x][y]) # 거리 출력
        break

    for i in range(4): # dfs 와 동일하게 진행함. 주변 x,y탐색하는 법
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if visited[nx][ny] == 0 and matrix[nx][ny] == '1':
                # 방문한 적이 없고, 인접한 곳일 경우(미로의 한 방향일 경우) 방문한다.
            visited[nx][ny] = visited[x][y] + 1 # 이동했으므로 거리에 1을 더해준다.
            queue.append((nx,ny)) # 방문했으므로 queue에 등록한다.


