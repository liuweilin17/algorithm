###########################################
# Let's Have Some Fun
# File Name: 53.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Nov 13 17:58:39 2018
###########################################
#coding=utf-8
#!/usr/bin/python

import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = (-1)*sys.maxsize
        maxSum = (-1)*sys.maxsize
        start = 0 # starting point in subarray with maximum value
        end = 0 # ending point in subarray with maximum value
        p = 0
        for i in range(len(nums)):
            if sum < 0: #如果当前和小于0，直接从当前数字重新开始计算和
                sum = nums[i]
                p = i
            else: #否则继续加
                sum += nums[i]
            if sum > maxSum: #更新maxSum
                maxSum = sum
                start = p
                end = i
        return maxSum

    # dynamic programming
    # f[i] is the max value of subarray ending at i
    # the optimal solution is max(f)
    def maxSubArray1(self, nums):
        l = len(nums)
        f = [1] * l
        for i in range(l):
            if i == 0:
                f[i] = nums[i]
            else:
                if f[i-1] > 0:
                    f[i] = f[i-1] + nums[i]
                else:
                    f[i] = nums[i]
        return max(f)

if __name__ == '__main__':
    s = Solution()
    a = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(a))
    print(s.maxSubArray1(a))
    print(s.maxSubArray([-1]))
    print(s.maxSubArray1([-1]))
