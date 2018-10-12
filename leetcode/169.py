###########################################
# Let's Have Some Fun
# File Name: 169.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Oct 12 18:18:14 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 169. Majority Element

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = None
        count = 0
        for i in nums:
            if num == None:
                num = i
                count = 1
            else:
                if i == num:
                    count += 1
                else:
                    count -= 1
                if count <= 0:
                    num = None
                    count = 0
            #print num, count
        return num

if __name__ == '__main__':
    s = Solution()
    print s.majorityElement([3,2,3])
    print s.majorityElement([2,2,1,1,1,2,2])
    print s.majorityElement([3,3,4])
    case1 = [47,47,72,47,72,47,79,47,12,92,13,47,47,83,33,15,18,47,47,47,47,64,47,65,47,47,47,47,70,47,47,55,47,15,60,47,47,47,47,47,46,30,58,59,47,47,47,47,47,90,64,37,20,47,100,84,47,47,47,47,47,89,47,36,47,60,47,18,47,34,47,47,47,47,47,22,47,54,30,11,47,47,86,47,55,40,49,34,19,67,16,47,36,47,41,19,80,47,47,27]
    print s.majorityElement(case1)
