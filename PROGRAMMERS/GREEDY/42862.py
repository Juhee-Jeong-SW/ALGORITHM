# 처음 idea : 가져오지 않은 사람에 대하여 reserve 앞과 비교해서 두 수의 차의 절대값이 1 이면 count를 증가시켜주고 reserve 앞은 제거해줌. ( 이미 빌려준 거니까 ) -> 2,3,5,7,12 테스트 케이스 실패
# -> 5, 7, 12 테스트 케이스 중 5, 12는 첫번째 for 문 차집합으로 변경하여 해결
# -> 7번 케이스는 sort()를 통하여 해결 (왜 해결된 건지 모를... )

def solution(n, lost, reserve):
    answer = 0

    count = n - len(lost)

    new_lost = []
    new_reserve = []

    if len(lost) == n and len(reserve) == n:
        return n

    for i in lost:
        if i in reserve:
            new_lost.append(i)
            new_reserve.append(i)
            count += 1

    lost = [x for x in lost if x not in new_lost]  # 중복 값 제거
    reserve = [x for x in reserve if x not in new_reserve]  # 중복값 제거

    lost.sort()
    reserve.sort()
    for i in lost:
        for j in reserve:
            if abs(i - j) == 1:
                count += 1
                reserve.remove(j)

    answer = count
    return answer