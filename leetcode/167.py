###########################################
# Let's Have Some Fun
# File Name: 167.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Jan 15 19:51:58 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 167. Two Sum II - Input array is sorted

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(numbers)
        i = 0
        j = l - 1
        while i<j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i+1, j+1]

