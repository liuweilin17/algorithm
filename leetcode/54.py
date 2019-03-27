###########################################
# Let's Have Some Fun
# File Name: 54.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Mar 26 16:58:17 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#54. Spiral Matrix

class Solution:
    def spiralOrder1(self, matrix: List[List[int]]) -> List[int]:
        N = len(matrix)
        if not N: return []
        M = len(matrix[0])
        t = (min(N, M) + 1) // 2
        ret = []
        for i in range(t):
            for j in range(i, M-i):
                ret.append(matrix[i][j])

            for j in range(i+1, N-i-1):
                ret.append(matrix[j][M-i-1])

            if N-i-1 != i: # Notice !!!
                for j in range(M-i-1, i-1, -1):
                    ret.append(matrix[N-i-1][j])
            if M-i-1 != j: # Notice !!!
                for j in range(N-i-2, i, -1):
                    ret.append(matrix[j][i])

        return ret

    # simulation
    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        r, c, dd = 0, 0, 0
        
        N = len(matrix)
        if not N: return []
        M = len(matrix[0])
        seen = [[False] * M for _ in matrix]
        ret = []
        
        for _ in range(N * M):
            ret.append(matrix[r][c])
            seen[r][c] = True
            
            # find the next r and c
            tr = r + dr[dd]
            tc = c + dc[dd]
            if 0<=tr<N and 0<=tc<M and not seen[tr][tc]:
                r, c = tr, tc
            else:
                dd = (dd+1) % 4
                r += dr[dd]
                c += dc[dd]
        return ret


