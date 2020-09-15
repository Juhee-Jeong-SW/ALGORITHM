# 내 idea : 접근법 자체가 떠오르지 않는다..
# 참고한 idea : 집합의 성질을 이용하여 다양한 경우의 수를 따진다.
""" N을 1번 사용할 경우 -> 5 (1번set)
    N을 2번 사용할 경우 -> 55 U (1번set과 1번set 사칙연산)
    N을 3번 사용할 경우 -> 555 U (1번set과 2번set U 2번set과 1번set)
    N을 4번 사용할 경우 -> 5555 U (1번set과 3번set U 2번과 2번 U 3번과 1번)
        ** 사칙연산 시 앞뒤 자리가 바뀌면 계싼 결과가 달라지는 것을 고려함.

        ...
    ==> N번을 n번 사용할 경우 -> n번만큼 숫자 붙이기 U (1번과 n-1번 U 2번과 n-2번.... U n-1번과 1번)

    출처 : https://gurumee92.tistory.com/164
"""


def solution(N, number):
    answer = -1
    DP = []

    for i in range(1, 9):  # 8번의 조합까지만 허용.
        numbers = set()
        numbers.add(int(str(N) * i))  # 그냥 붙이는 경우.

        for j in range(0, i - 1):
            for x in DP[j]:
                for y in DP[-j - 1]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)
                    if y != 0:
                        numbers.add(x // y)

        if number in numbers:
            answer = i
            break

        DP.append(numbers)

    return answer