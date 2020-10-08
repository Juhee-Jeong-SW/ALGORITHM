#-*- encoding: utf-8 -*-
"""시험 감독"""

import sys

n = int(sys.stdin.readline())
applicants = list(map(int,sys.stdin.readline().split(' ')))
b, c = map(int, sys.stdin.readline().split(' '))
answer = 0

for num in applicants:
    if num >= b:
        num -= b # 총 감독꽌 우선 다 빼주기
        if num % c == 0: #줌 부감독관을 구하기 위한 것. 딱 맞아 떨어지면 몫만 더하고
            answer += (num // c)
        else:
            answer += (num // c) + 1 # 나머지가 있다면 그만큼 더 해줘야하니까 1더해

print(answer + n) # 시험 감독관은 무조건 참여하므로 그만큼 다시 더해줌



# 실패 코드
# chong = [0] * len(a)
# buChong = [0] * len(a)
#
# for i in range(len(a)):
#     a[i] = (a[i] - b)
#     chong[i] += 1
#
# for i in range(len(a)):
#     if a[i] == 0:
#         break
#     elif a[i] <= c :
#         buChong[i] = 1
#     else :
#         buChong[i] = (a[i] // c) + 1
#
# sum = 0
#
# for i in chong:
#     sum += i
# for j in buChong:
#     sum += j
#
# print(sum)

