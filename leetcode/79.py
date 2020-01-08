###########################################
# Let's Have Some Fun
# File Name: 79.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Mar 26 09:26:02 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#79. Word Search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N = len(board)
        if not N: return False
        M = len(board[0])
        track = []

        def backtrack(N, M, track, word):
            if not len(word): return True
            n, m = track[-1]
            #print('{},{},{},{},{},{}'.format(track, word, N, M, n, m))
            if n + 1 < N and (n+1, m) not in track:
                if board[n+1][m] == word[0]:
                    if backtrack(N, M, track + [(n+1, m)], word[1:]):
                        return True
            if n - 1 >= 0 and (n-1, m) not in track:
                if board[n-1][m] == word[0]:
                    if backtrack(N, M, track + [(n-1, m)], word[1:]):
                        return True
            if m + 1 < M and (n, m+1) not in track:
                if board[n][m+1] == word[0]:
                    if backtrack(N, M, track + [(n, m+1)], word[1:]):
                        return True
            if m - 1 >= 0 and (n, m-1) not in track:
                if board[n][m-1] == word[0]:
                    if backtrack(N, M, track + [(n, m-1)], word[1:]):
                        return True
            return False

        for i in range(N):
            for j in range(M):
                if board[i][j] == word[0]:
                    if backtrack(N, M, track + [(i, j)], word[1:]):
                        return True
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS
        visited = [] # the index of used grid
        N = len(board)
        if not N: return False
        M = len(board[0])
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        def dfs(word, x, y): # whether word could be matched beginning with (x,y)
            if not word:
                return True
            elif word[0] != board[x][y]:
                return False
            else:
                visited.append((x, y))
                for k in range(4):
                    xx, yy = x + dx[k], y + dy[k]
                    if (xx, yy) not in visited and 0<=xx<N and 0<=yy<M:
                        if dfs(word[1:], xx, yy):
                            return True
                visited.pop()
                return True if not word[1:] else False

        for i in range(N):
            for j in range(M):
                if dfs(word, i, j):
                    return True
        return False


