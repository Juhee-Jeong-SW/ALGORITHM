import heapq


def solution(scoville, K):
    answer = 0
    heap = []
    count, flag = 0, 0

    for i in scoville:
        heapq.heappush(heap, i)

    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (2 * heapq.heappop(heap)))
        except IndexError:
            return -1
        count += 1

    return count

#     answer = 0
#     heapq.heapify(scoville)
#     temp1, temp2, sco = 0, 0, 0
#     count = 0
#     flag = 0

#     while scoville[0] < K :
#         temp1 = heapq.heappop(scoville)
#         temp2 = heapq.heappop(scoville)
#         sco = temp1 + (temp2 * 2)
#         heapq.heappush(scoville, sco)

#         if len(scoville) == 1 and scoville[0] < K :
#             flag = 1
#             break

#         count += 1

#     if flag == 1 :
#         return -1
#     else :
#         return count