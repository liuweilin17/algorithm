###########################################
# Let's Have Some Fun
# File Name: 1072.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun  2 Jun 22:09:36 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#1072. Flip Columns For Maximum Number of Equal Rows

class Solution:
    # the way of calculating the pattern is the key
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        M = len(matrix[0])

        lst = []
        for i in range(N):
            pattern = []
            for j in range(M):
                pattern.append(matrix[i][0] ^ matrix[i][j])
            lst.append(tuple(pattern))

        dt = collections.Counter(lst)
        return max(dt.values())


