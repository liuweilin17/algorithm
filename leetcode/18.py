###########################################
# Let's Have Some Fun
# File Name: 18.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Jan 15 21:44:13 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 18. 4Sum
# similar questions:   454

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()
        l = len(nums)
        dt = {}
        ret = set([])
        for i in range(l-1):
            for j in range(i+1, l):
                s = nums[i] + nums[j]
                if s in dt.keys():
                    dt[s].append((i, j))
                else:
                    dt[s] = [(i, j)]
        #print(dt)

        for i in range(l-1):
            for j in range(i+1, l):
                s = target - nums[i] - nums[j]
                if s in dt.keys():
                    for p,q in dt[s]:
                        if p > j:
                            ret.add((nums[i], nums[j], nums[p], nums[q]))

        return list(map(list, ret))

if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1,0,-1,0,-2,2], 0))
