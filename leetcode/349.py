###########################################
# Let's Have Some Fun
# File Name: 349.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Sep  5 18:10:08 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#349. Intersection of Two Arrays

class Solution:
    def intersection1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # sort and binary search
        a1 = sorted(list(set(nums1)))
        a2 = sorted(list(set(nums2)))
        N = len(a2)
        ret = []
        for e in a1:
            left, right = 0, N-1
            flag = False
            while left <= right:
                mid = (left+right)//2
                if a2[mid] > e:
                    right = mid-1
                elif a2[mid] < e:
                    left = mid+1
                else:
                    flag = True
                    break
            if flag:
                ret.append(e)

        return ret

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1)-(set(nums1)-set(nums2)))
