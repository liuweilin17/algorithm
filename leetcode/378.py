###########################################
# Let's Have Some Fun
# File Name: 378.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Jan 20 17:31:15 2019
###########################################
#coding=utf-8
#!/usr/bin/python

import heapq

class Solution:
    # my own method
    def kthSmallest1(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        a = [0] * m

        minInd = -1
        minV = float('inf')

        for i in range(k):
            minV = float('inf')
            for j in range(m):
                if a[j] == -1: continue
                if matrix[j][a[j]] <= minV:
                    minInd, minV = j, matrix[j][a[j]]
            if a[minInd] == n-1:
                a[minInd] = -1
            else:
                a[minInd] += 1
            #print(minV)

        return minV

    # use heap to simplify.
    # The method is actually the same with my own method, but much faster
    def kthSmallest2(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l = len(matrix[0])
        # (v, R, ind), v is the value of each row, ind is the next value
        h = [(row[0], row, 1) for row in matrix]

        heapq.heapify(h)
        for i in range(k-1):
            v, R, i = h[0]
            if i < l:
                heapq.heapreplace(h, (R[i], R, i+1))
            else:
                heapq.heappop(h)

        return h[0][0]

if __name__ == '__main__':
    s = Solution()
    print(s.kthSmallest2([[1,5,9],[10,11,13],[12,13,15]], 8))
