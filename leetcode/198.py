###########################################
# Let's Have Some Fun
# File Name: 198.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Nov 14 17:48:10 2018
###########################################
#coding=utf-8
#!/usr/bin/python

#198. House Robber

class Solution(object):
    # dynamic programming, O(n2)
    # d[i] represents the max sum of robbing sequence ending with d[i]
    def rob1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l < 1:
            return None
        if l < 2:
            return nums[l-1]
        d = [0] * l
        d[0] = nums[0]
        d[1] = nums[1]
        for i in range(2,l):
            maxV = -1
            for j in range(i-1):
                if d[j] > maxV:
                    maxV = d[j]
            d[i] = maxV + nums[i]
        return max(d)

    # dynamic programming, O(n)
    # d[i] represents the max sum of robbing subsequence from 0 to i-1
    # if nums[i] is robbed, d[i+1] = d[i-1] + nums[i]
    # if nums[i] is not robbed, d[i+1] = d[i]
    def rob2(self, nums):
        l = len(nums)
        d = (l + 1) * [0]
        if l<1:
            return 0
        d[1] = nums[0]
        for i in range(1,l):
            d[i+1] = max(d[i], d[i-1] + nums[i])
        return d[l]

if __name__ == '__main__':
    s = Solution()
    print(s.rob1([1,2,3,1]))
    print(s.rob2([1, 2, 3, 1]))
    print(s.rob1([2,7,9,3,1]))
    print(s.rob2([2, 7, 9, 3, 1]))
