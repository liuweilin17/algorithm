###########################################
# Let's Have Some Fun
# File Name: 4.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Sep 12 21:18:40 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#4. Median of Two Sorted Arrays

class Solution:
    # method 1, simple but not good enough
    # O((m+n)log(m+n))
    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1 + nums2
        a.sort()
        N = len(a)
        return (a[(N-1)//2]+a[N//2])/2
    
    # method 2, O(log(min(m,n)))
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n: # make nums1 smaller
            nums1, nums2, m, n = nums2, nums1, n, m

        imin, imax = 0, m
        half = (m + n + 1) // 2 # left size might = right size + 1
        while imin <= imax:
            i = (imax + imin) // 2
            j = half - i
            if i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                # find max left
                max_left = None
                if i == 0: max_left = nums2[j-1]
                elif j == 0: max_left = nums1[i-1]
                else: max_left = max(nums2[j-1], nums1[i-1])
                if (m + n) % 2 == 1:
                    return max_left
                
                # find min right
                min_right = None
                if i == m: min_right = nums2[j]
                elif j == n: min_right = nums1[i]
                else: min_right = min(nums2[j], nums1[i])
                
                return (max_left + min_right) / 2

