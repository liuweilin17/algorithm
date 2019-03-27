###########################################
# Let's Have Some Fun
# File Name: 59.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Mar 26 17:40:19 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 59. Spiral Matrix II

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret = [[-1] * n for _ in range(n)]

        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        r, c, dd = 0, 0, 0

        for i in range(1, n**2+1):
            #print('{}{}'.format(r, c))
            ret[r][c] = i
            tr = r + dr[dd]
            tc = c + dc[dd]
            if 0<=tr<n and 0<=tc<n and ret[tr][tc] == -1:
                r = tr
                c = tc
            else:
                dd = (dd + 1) % 4
                r += dr[dd]
                c += dc[dd]

        return ret

