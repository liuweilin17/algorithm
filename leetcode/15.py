###########################################
# Let's Have Some Fun
# File Name: 15.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Jan 15 20:47:46 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 15. 3Sum

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []

        ret = set([])
        l = len(nums)
        nums.sort()
        for i in range(l-2):
            begin = i+1
            end = l-1
            remain = 0-nums[i]
            while begin < end:
                if nums[begin] + nums[end] < remain:
                    begin += 1
                elif nums[begin] + nums[end] > remain:
                    end -= 1
                else:
                    ret.add((nums[i], nums[begin], nums[end]))
                    begin += 1 # notice !!!
        return list(map(list, ret)) # no duplicate !!!

if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))
    print(s.threeSum([0,0,0,0]))
    print(s.threeSum([]))
