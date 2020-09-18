#-*- encoding: utf-8 -*-
"""부녀회장이 될테야"""
#idea : 3층 3호에 사는 사람은 3층 2호 + 2층 3호 / 3층 2호 는 2층 1호 + 2층 2호

cases = int(input())

for _ in range(cases) :
    k = int(input()) # 층 (0층~)
    n = int(input()) # 호 (1호~)
    apart = [v for v in range(1,n+1)]

    for i in range(k) :
        for j in range(1, n) :
            apart[j] += apart[j-1]

    print(apart[n-1])

""" 두번째 시도

def solve(k, n) :
    answer = 0
    if k == 1 :
        for i in range(1, n+1) :
            answer += i
        return answer
    else :
        for j in range(1, n+1) : # k층 n호는 k-1층 1부터 n호까지의 합
            answer += solve(k-1, j)
        return answer


cases = int(sys.stdin.readline()) # 케이스 개수

for _ in range(cases) :
    k = int(input())  # 층 (0층~)
    n = int(input())  # 호 (1호~)

    print(solve(k, n))
"""


