# idea : 모든 리스트를 돌며 조건에 맞으면 count를 증가시킨다. (스택 이용하지 않음..)

def solution(prices):
    answer = []

    for i in range(0, len(prices)):
        count = 0
        # top = prices.pop(0)
        for j in range(i + 1, len(prices)):
            if prices[j] >= prices[i]:
                count += 1
            else:
                count += 1
                break
        answer.append(count)

    return answer