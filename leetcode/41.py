###########################################
# Let's Have Some Fun
# File Name: 41.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Sep 19 17:58:26 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#41. First Missing Positive

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # use nums[a]'s negative value to remember a exits
        if 1 not in nums:
            return 1

        N = len(nums)
        # replace all the 0, negative and >N elements with 1
        for i in range(N):
            if nums[i] <= 0 or nums[i] > N:
                nums[i] = 1

        for a in nums:
            a = abs(a)
            if a == N:
                nums[0] = -abs(nums[0]) # nums[0] might be changed several times
            else:
                nums[a] = -abs(nums[a])

        print(nums)
        for i in range(1, N):
            if nums[i] > 0:
                return i

        if nums[0] > 0:
            return N

        return N+1

