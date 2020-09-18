#-*- encoding: utf-8 -*-
"""달팽이는 올라가고 싶다"""
#idea : 정상에 올라갈 때까지 차이만큼 나누어서 얼마나 걸리는지 계산함. 주의할 점은 정상에서는 떨어지지 않고 버티고 있음.

import sys

A, B, V = map(int, sys.stdin.readline().split(' '))

days = (V-B) / (A-B) # 정상에서는 낮에만 올라가도 1일 추가되니까 B만큼 빼주어도 됨.

if days % 1 > 0 : # 나머지가 있다면 하루 더 가야하므로
    print(int(days) + 1)
else :
    print(int(days))



"""두번째 시도"""
# for i in range((V//diff+1)) :
#     if i * diff >= V :
#         print(i-1)
#         break

"""첫번째 시도"""
# while True :
#     sum += diff
#     count += 1
#     if sum > V :
#         print(count-1)
#         break