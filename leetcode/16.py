###########################################
# Let's Have Some Fun
# File Name: 16.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Jan 15 21:20:27 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 16. 3Sum Closest

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        l = len(nums)
        minV = float('inf')
        ret = 0
        for i in range(l-2):
            start = i+1
            end = l-1
            while start < end:
                s = nums[i] + nums[start] + nums[end]
                if s > target:
                    end -= 1
                elif s < target:
                    start += 1
                else:
                    return s
                if abs(s - target) < minV:
                    minV = abs(s - target)
                    ret = s

        return ret

if __name__ == '__main__':
    s = Solution()
    #print(s.threeSumClosest([-1,2,1,-4], 1))
    #print(s.threeSumClosest([0, 1, 2], 3))
    #print(s.threeSumClosest([1,2,5,10,11], 12))
    print(s.threeSumClosest([1,6,9,14,16,70], 81))
