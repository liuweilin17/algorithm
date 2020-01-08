###########################################
# Let's Have Some Fun
# File Name: 97.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Oct 13 12:55:47 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#97. Interleaving String

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N1, N2, N3 = len(s1), len(s2), len(s3)
        dp = [[[0 for _ in range(N3+1)] for _ in range(N2+1)] for _ in range(N1+1)]

        def helper(x, y, z): # whether s3[z:] is formed by s1[x:] and s2[y:]
            if dp[x][y][z] != 0:
                return True if dp[x][y][z] == 1 else False
            if x == len(s1) and y == len(s2) and z == len(s3):
                dp[x][y][z] = 1
                return True

            # compare with s1
            if x < len(s1) and z < len(s3) and s1[x] == s3[z]:
                if helper(x+1, y, z+1):
                    dp[x][y][z] = 1
                    return True
            # compare s2 with s3
            if y < len(s2) and z < len(s3) and s2[y] == s3[z]:
                if helper(x, y+1, z+1):
                    dp[x][y][z] = 1
                    return True

            dp[x][y][z] = -1
            return False

        return helper(0, 0, 0)




