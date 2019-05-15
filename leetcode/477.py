###########################################
# Let's Have Some Fun
# File Name: 477.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat 11 May 16:35:52 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#477. Total Hamming Distance

# For each bit in 32-bit integer, we calculate the number of ones of N number as M.
# Then the difference in this bit is M * (N - M)

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ret = 0
        N = len(nums)
        for i in range(32):
            ones = 0
            for j in range(N):
                ones += (nums[j] >> i) & 1
            ret += ones * (N - ones)

        return ret
