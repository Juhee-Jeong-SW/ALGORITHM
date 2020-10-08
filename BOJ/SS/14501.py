#-*- encoding: utf-8 -*-
"""퇴사"""
#idea : dp를 이용하여 상담 진행 날짜에 대한 비용을 쌓아가며 증가시킨다. 입력된 day에 해당하는 값을 출력한다.

import sys

day = int(sys.stdin.readline())
time = [0] * day
pay = [0] * day
dp = [0] * 25 # 15로 하면 runtime error 남..

for i in range(day):
    time[i], pay[i] = map(int, sys.stdin.readline().split(' '))


for i in range(day):
    if dp[i] > dp[i+1]: # 현재의 비용이 다음 비용보다 크면
        dp[i+1] = dp[i] # 다음 비용에는 현재 비용을 넣어준다. (큰 값으로 채우기)

    if dp[i + time[i]] < dp[i] + pay[i]:
        # 현재로부터 상담이 마무리된 시점의 비용과 현재 비용에 현재 상담을 더한 값을 비교하여 전자가 작다면
        dp[i + time[i]] = dp[i] + pay[i] # 전자에는 큰 값을 갱신시킬 수 있도록 넣어준다.


print(dp[day])

