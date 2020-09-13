#-*- encoding: utf-8 -*-
"""트리 순회"""
#처음 idea : 트리 부모 찾기처럼 dfs 접근하기 위해 인접 행렬을 그려서 하려고 했으나 실패
#찾아본 idea : 재귀 함수를 이용하여 순회 순서에 맞게 호출해준다. 트리는 딕셔너리를 이용해 그릴 수 있다.
#참조 : https://suri78.tistory.com/134

import sys

# 전위 : C - L - R
# 중위 : L - C - R
# 후위 : L - R - C
n = int(sys.stdin.readline())
tree = {}

def preorder(node) : # 전위
    if node == '.' :
        return
    print(node, end="")
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node) : # 중위
    if node == '.' :
        return
    inorder(tree[node][0])
    print(node, end="")
    inorder(tree[node][1])


def postorder(node) : # 후위
    if node == '.' :
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end="")

# 트리 만들기 : 딕셔너리 형태 -> 루트 : 키 자식노드 : 벨류
for _ in range(n) :
    root, left, right = map(str, sys.stdin.readline().split())
    tree[root] = (left, right)


preorder('A')
print()
inorder('A')
print()
postorder('A')
