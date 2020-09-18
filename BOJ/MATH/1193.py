#-*- encoding: utf-8 -*-
"""분수찾기"""
#idea : 분수 해당하는 규칙이 존재함. (1/1) (1/2,2/1) (3/1,2/2,1/3) (1/4,2/3,3/2,4/1) ...
# sum이 N보다 커질 때 멈추는데, sum은 분수의 묶음의 가장 마지막을 나타낸다. 그래서 그에 대한 차이를 구해 분수 묶음만 계산할 수 있게 한다.

import sys

N = int(sys.stdin.readline())
sum = 0
i = 0
diff = 0

while True :
    sum += ( i + 1 )
    if N <= sum :
        diff = sum - N
        if i % 2 == 0 :
            answer = str(1+diff)+"/"+str((i+1)-diff)
            print(answer)
            break
        else :
            answer = str((i+1)-diff)+"/"+str(1+diff)
            print(answer)
            break
    else :
        i += 1
