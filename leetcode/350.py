###########################################
# Let's Have Some Fun
# File Name: 350.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Oct 30 11:52:12 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 350. Intersection of Two Arrays II
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l1 = len(nums1)
        l2 = len(nums2)
        rec = []
        ret = []
        for i in range(l1):
            n1 = nums1[i]
            for j in range(l2):
                n2 = nums2[j]
                if n2 == n1 and j not in rec:
                    ret.append(n2)
                    rec.append(j)
                    break 
        return ret

if __name__ == '__main__':
    s = Solution()
    #nums1 = [1,2,2,1]
    #nums2 = [2,2]
    #print s.intersect(nums1,nums2)
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print s.intersect(nums1,nums2)

