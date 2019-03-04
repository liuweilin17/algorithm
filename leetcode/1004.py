###########################################
# Let's Have Some Fun
# File Name: 1004.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Mar  3 21:00:23 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#1004. Max Consecutive Ones III

class Solution:
    def longestOnes1(self, A: List[int], K: int) -> int:
        res, zeros = 0, 0
        # [left right] is the consecutive ones with flipped ones.
        left = 0
        for right in range(len(A)):
            if A[right] == 0:
                zeros += 1
            while zeros > K:
                if A[left] == 0:
                    zeros -= 1
                left += 1
            res = max(right - left + 1, res)  # notice !!!, we update res with every new right
        return res

    # requires longer time
    # we use queue to memorize the position of zeros.
    def longestOnes2(self, A: List[int], K: int) -> int:
        res, left, zeros = 0, 0, 0
        N = len(A)
        Q = Queue()
        for right in range(N):
            if A[right] == 0:
                Q.put(right)
            if Q.qsize() > K:
                q = Q.get()
                left = q+1
            res = max(res, right-left+1)
        return res
