###########################################
# Let's Have Some Fun
# File Name: 238.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Dec 30 18:25:04 2018
###########################################
#coding=utf-8
#!/usr/bin/python
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        l = len(nums)
        res = [1] * l
        p = 1
        # calculate the product of elements before i
        for i in range(l):
            res[i] *= p
            p *= nums[i]

        # calculate the product of elements after i
        p = 1
        for i in range(l-1, -1, -1):
            res[i] *= p
            p *= nums[i]

        return res




if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))
