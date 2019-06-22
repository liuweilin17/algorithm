from queue import Queue

# 1091. Shortest Path in Binary Matrix

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[N-1][M-1] == 1: return -1
        
        # BFS
        q = Queue()
        q.put((0, 0, 1))
        dx = [0, 0, 1, 1, 1, -1, -1, -1]
        dy = [1, -1, -1, 0, 1, -1, 0, 1]
        while not q.empty():
            i, j, d = q.get()
            for k in range(8):
                x, y = i+dx[k], j+dy[k]
                if 0<=x<N and 0<=y<M and grid[x][y] == 0:
                    if x == N-1 and y == M-1: return d+1
                    grid[x][y] = 1
                    q.put((x, y, d+1))
                    
        return -1
