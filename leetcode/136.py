###########################################
# Let's Have Some Fun
# File Name: 136.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Nov 11 16:17:40 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 136. Single Number
# xor 异或 操作

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for i in nums:
            ret ^= i
        return ret

if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([2,2,1]))
    print(s.singleNumber([4,1,2,1,2]))
