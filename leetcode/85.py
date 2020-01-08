###########################################
# Let's Have Some Fun
# File Name: 85.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Oct 11 10:27:09 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#85. Maximal Rectangle

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        N = len(matrix)
        if not N: return 0
        M = len(matrix[0])
        dp = [[0 for _ in range(M)] for _ in range(N)] #consecutive 1s in rows
        # calculate consecutive 1s in each row
        for i in range(N):
            for j in range(M):
                if j == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    if matrix[i][j] == "0":
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i][j-1] + 1

        # calculate maximum area ending at each point
        max_area = 0
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == "1":
                    width = j+1
                    height = 0
                    for k in range(i, -1, -1):
                        width = min(width, dp[k][j])
                        if width == 0: break
                        height += 1
                        max_area = max(max_area, width*height)


        return max_area



