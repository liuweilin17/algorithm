###########################################
# Let's Have Some Fun
# File Name: 278.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Mar  2 21:12:31 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#278. First Bad Version

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    # find the left most true with binary search
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low
        # if low >=1 and low <= n and isBadVersion(low):
        #     return low
        # else:
        #     return -1

