###########################################
# Let's Have Some Fun
# File Name: 1162.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun 18 Aug 11:02:07 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#1162. As Far from Land as Possible

from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # simply use layer bfs beginning with all the 1's
        # after 0 is found among the neighbors, add it to queue and set it to 1
        # the final level is the result !!!

        N, M = len(grid), len(grid[0])

        q = deque([(i, j) for i in range(M) for j in range(N) if grid[i][j] == 1])
        if len(q) == M * N or len(q) == 0: return -1
        level = 0
        while q:
            n = len(q)
            for _ in range(n):
                x, y = q.popleft()
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    xx, yy = x+dx, y+dy
                    if 0 <= xx < N and 0 <= yy < M and grid[xx][yy] == 0:
                        q.append((xx, yy))
                        grid[xx][yy] = 1
            level += 1

        return level-1


