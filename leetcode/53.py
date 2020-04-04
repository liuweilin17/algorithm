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
    # DP, O(n) time, O(n) space
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i]: the largest sum ending at nums[i]
        ret = 0
        if not nums: return 0
        N = len(nums)
        dp = [0 for _ in range(N)]
        dp[0] = nums[0]
        for i in range(1, N):
            dp[i] = max(dp[i-1]+nums[i], nums[i])

        return max(dp)

    # DP, O(n) time, O(n) space
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        N = len(nums)
        cur = nums[0] # current max ending at the current position
        ret = cur
        for i in range(1, N):
            cur = max(nums[i], cur+nums[i])
            ret = max(cur, ret) 
        return ret

    # Divide and Conquer
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(begin, end):
            if begin == end: 
                return nums[begin]
            # return max subarray from begin to end
            mid = (begin + end) // 2
            leftMax = helper(begin, mid)
            rightMax = helper(mid+1, end)
            crossMax1 = float('-inf')
            t = 0
            for i in range(mid, begin-1, -1):
                t += nums[i]
                crossMax1 = max(crossMax1, t)
            crossMax2 = float('-inf')
            t = 0
            for i in range(mid+1, end+1):
                t += nums[i]
                crossMax2 = max(crossMax2, t)
            if crossMax1 == float('-inf'): crossMax1 = 0
            if crossMax2 == float('-inf'): crossMax2 = 0
            
            return max([leftMax, rightMax, crossMax1+crossMax2])
                
        N = len(nums)
        return helper(0, N-1)

if __name__ == '__main__':
    s = Solution()
    a = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(a))
    print(s.maxSubArray1(a))
    print(s.maxSubArray([-1]))
    print(s.maxSubArray1([-1]))
