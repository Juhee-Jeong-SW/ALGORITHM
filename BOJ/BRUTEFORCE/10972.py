#-*- encoding: utf-8 -*-
"""다음 순열"""

import sys


def next_permutation(nums, n):
    i = n - 1

    while i > 0 and nums[i-1] >= nums[i]: # > (내림차순이니까) 를 만족하지 않는 i-1 찾기
        i -= 1
    if i <= 0: # 마지막 순열인 경우
        return False

    j = n - 1
    while nums[j] <= nums[i-1]:# i-1보다 큰 j 찾기
        j -= 1

    nums[j], nums[i-1] = nums[i-1], nums[j]

    j = n - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

    return True


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split(' ')))


if next_permutation(nums, n) is True:
    for i in nums:
        print(i, end=" ")
else:
    print(-1)

