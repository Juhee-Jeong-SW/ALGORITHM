# idea ; 두수를 뺀 값이 양수냐 음수냐에 따라 나누어 합산을 해준다.

def solution(a, b):
    answer = 0

    minus = b - a
    sum = 0

    if minus > 0:
        for i in range(a, b + 1, 1):
            sum += i

    elif minus < 0:
        for i in range(a, b - 1, -1):
            sum += i

    elif minus == 0:
        sum = a

    answer = sum
    return answer