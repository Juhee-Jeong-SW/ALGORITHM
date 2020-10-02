#-*- encoding: utf-8 -*-
"""이전 순열"""
import sys


def prior_permutation(nums, n):
    i = n - 1

    while i > 0 and nums[i-1] <= nums[i]:
        i -= 1

    if i <= 0:
        return False

    j = n - 1

    while nums[j] >= nums[i-1]:
        j -= 1

    nums[i-1], nums[j] = nums[j], nums[i-1]

    j = n - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

    return True


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split(' ')))


if prior_permutation(nums, n) is True:
    for i in nums:
        print(i, end=" ")
else:
    print(-1)
