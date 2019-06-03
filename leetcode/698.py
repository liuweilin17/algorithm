###########################################
# Let's Have Some Fun
# File Name: 698.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat  1 Jun 12:16:16 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#698. Partition to K Equal Sum Subsets

class Solution:
    #https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/108730/JavaC%2B%2BStraightforward-dfs-solution
    def canPartitionKSubsets1(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        if N < k: return False
        sumV = sum(nums)
        if sumV % k != 0:
            return False
        target = sumV // k

        visited = [0] * N

        def helper(tmp, count, ind, k): # Notice ind is necessary!
            if k == 1: return True
            if tmp == target and count > 0:
                return helper(0, 0, 0, k-1)
            for i in range(ind, N):
                if visited[i] == 0:
                    visited[i] = 1
                    if helper(tmp+nums[i], count+1, i+1, k): return True
                    visited[i] = 0
            return False

        return helper(0, 0, 0, k) 


