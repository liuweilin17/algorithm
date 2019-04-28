###########################################
# Let's Have Some Fun
# File Name: 1034.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Apr 28 16:38:33 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 1034. Coloring A Border

class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        components = []
        border = []
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        M, N = len(grid), len(grid[0])

        def dfs(r, c):
            if not (0<=r<M and 0<=c<N and grid[r][c] == grid[r0][c0]): return False

            if (r, c) in components: return True

            components.append((r, c))

            # Notice, we use dfs to find all the border in the same time
            if (dfs(r, c+1) + dfs(r, c-1) + dfs(r-1, c) + dfs(r+1, c)) < 4:
                border.append((r,c))

            return True

        dfs(r0, c0)
        for i, j in border:
            grid[i][j] = color

        return grid



