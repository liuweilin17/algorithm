###########################################
# Let's Have Some Fun
# File Name: 962.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Dec 28 21:27:48 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# some part of the algorithm refer to question 121
class Solution:
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = len(A)
        B = []
        for i in range(l):
            B.append((A[i], i))
        B = sorted(B, key=lambda x:x[0])
        minV = 50001
        maxRamp = -1
        for ele in B:
            if ele[1] < minV:
                minV = ele[1]
            if ele[1] - minV > maxRamp:
                maxRamp = ele[1] - minV
        return maxRamp



if __name__ == '__main__':
    s = Solution()
    print(s.maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))


