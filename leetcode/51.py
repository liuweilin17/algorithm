###########################################
# Let's Have Some Fun
# File Name: 51.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Sep 23 18:25:38 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#51. N-Queens
# And
#52. 52. N-Queens II

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # O(N!) time complexity

        ret = []
        cols = [0] * n
        diag1 = [0] *  (2*n - 1) # row + col fixed
        diag2 = [0] * (2*n - 1) # row - col fixed
        queen = set()

        def helper(row, queen, n): # add a queen to row
            for col in range(n):
                if not (cols[col] + diag1[row+col] + diag2[row-col+n-1]):
                    queen.add((row, col))
                    cols[col] = 1
                    diag1[row+col] = 1
                    diag2[row-col+n-1] = 1
                    if row == n-1:
                        tmp = []
                        for r, c in sorted(queen):
                            tmp.append(c*'.' + 'Q' + (n-c-1)*'.')
                        ret.append(tmp)
                    else:
                        helper(row+1, queen, n)
                    cols[col] = 0
                    diag1[row+col] = 0
                    diag2[row-col+n-1] = 0
                    queen.remove((row, col))

        helper(0, queen, n)
        return ret

