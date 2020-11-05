#소수찾기

from itertools import permutations


def find_primeNum(num):
    pNumbers = []

    for n in num:
        count = 0
        for i in range(2, n):
            if n % i == 0:
                count += 1
                break
        if n > 1 and count == 0:
            pNumbers.append(n)

    return len(pNumbers)


def solution(numbers):
    answer = 0
    num_case = []

    for i in range(1, len(numbers) + 1):
        temp = permutations(numbers, i)

        for n in temp:
            temp_str = "".join(n)
            num_case.append(int(temp_str))

    num_case = list(set(num_case))

    answer = find_primeNum(num_case)
    return answer