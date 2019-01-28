###########################################
# Let's Have Some Fun
# File Name: 11.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Jan 27 17:19:15 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#11. Container With Most Water

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n-1
        maxV = -1
        while left < right:
            if height[left] < height[right]:
                area = height[left] * (right - left)
                if area > maxV: maxV = area
                left += 1
            else:
                area = height[right] * (right - left)
                if area > maxV: maxV = area
                right -= 1
        return maxV

