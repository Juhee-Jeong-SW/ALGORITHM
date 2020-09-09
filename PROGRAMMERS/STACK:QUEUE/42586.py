# idea : 작업 마치기까지 남은 양을 계산하여 남은 리스트를 순회하며 조건 확인. 현재가 전보다 작으면 전에 있는 걸 현재에 넣어줌. (전 부분이 끝날 떄까지 기다린다는 뜻)

import math


def solution(progresses, speeds):
    answer = []
    finish = []
    count = 1

    for i in range(0, len(progresses)):
        finish.append(math.ceil((100 - progresses[i]) / speeds[i]))
        # print(finish)
    print(finish)
    for i in range(1, len(finish)):
        if finish[i] < finish[i - 1]:
            finish[i] = finish[i - 1]

    print(finish)

    for i in range(1, len(finish)):
        if finish[i] <= finish[i - 1]:
            count += 1
        else:
            answer.append(count)
            count = 1

    answer.append(count)
    return answer