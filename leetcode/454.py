###########################################
# Let's Have Some Fun
# File Name: 454.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Jan 15 10:25:13 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 454. 4Sum II

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # first calcuate sum of two elements in A, B, then find -a-b in the sum of two elements in C, D
        sumDt = {}
        for a in A:
            for b in B:
                sumDt[a+b] = sumDt.get(a+b, 0) + 1

        ret = 0
        for c in C:
            for d in D:
               ret += sumDt.get(-c-d, 0)

        return ret


if __name__ == '__main__':
    s = Solution()
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(s.fourSumCount(A, B, C, D))
