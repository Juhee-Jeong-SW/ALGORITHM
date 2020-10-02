#-*- encoding: utf-8 -*-
"""모든 순열"""

import sys


def next_permutation(nums, n):
    i = n - 1

    while i > 0 and nums[i-1] >= nums[i] :
        i -= 1

    if i <= 0:
        return False

    j = n - 1
    while nums[j] <= nums[i-1]:
        j -= 1

    nums[i-1], nums[j] = nums[j], nums[i-1]

    j = n - 1

    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

    return True


N = int(sys.stdin.readline())
nums = [i+1 for i in range(N)]

while True:
    print(' '.join(map(str,nums)))
    if not next_permutation(nums, N):
        break
