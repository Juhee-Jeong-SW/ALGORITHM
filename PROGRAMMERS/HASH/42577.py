# 전화번호 목록
# idea : 먼저 정렬한 뒤 가장 앞에 있는 숫자가 접두어 역할을 하므로 그것이 있는지 파악함.

def solution(phone_book):
    answer = True

    phone_book.sort()

    for i in range(1, len(phone_book) - 1):
        if phone_book[0] in phone_book[i]:
            answer = False
            break
        answer = True

    return answer


""" 예전 코드
phone_book.sort()

for i in range(0, len(phone_book) - 1):
    if phone_book[i] in phone_book[i + 1][:len(phone_book[0])]:
        answer = False
        break
    answer = True

    """