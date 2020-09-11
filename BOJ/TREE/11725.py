#-*- encoding: utf-8 -*-
"""트리의 부모 찾기"""
#기존 생각한 idea : 연결리스트 개념을 이용하기 위해 입력값을 받으면서 존재 여부 조건 확인 후 왼쪽, 오른쪽에 붙여넣으려고 했음.
#찾은 idea : 트리를 그래프 형태로 구현한 후, 부모 노드를 찾는 방식. but 그래프처럼 순회는 아니고 한 방향으로만 탐색하므로 visited는 제거
#참조 : https://developmentdiary.tistory.com/435

import sys
sys.setrecursionlimit(10 ** 9) # 재귀 함수의 최대 깊이를 늘려줘야 함. 기본적으로 1000레벨 <- 런타임에러 해결방법

n = int(sys.stdin.readline())
node_graph = [[] for _ in range(n+1)]

for _ in range(n-1) :
    i, j = map(int, sys.stdin.readline().split())
    node_graph[i].append(j)
    node_graph[j].append(i)

parent = [0 for _ in range(n+1)]

def dfs(start, node_graph, parent) :
    for i in node_graph[start] :
        if parent[i] == 0 :
            parent[i] = start
            dfs(i, node_graph, parent)


dfs(1, node_graph, parent)

for i in range(2, n+1) :
    print(parent[i])
