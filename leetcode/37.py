###########################################
# Let's Have Some Fun
# File Name: 37.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Sep 18 16:53:34 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#37. Sudoku Solver

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def helper(b):
            # print(b)
            # Given board b
            # return True if self.ret has been found
            for i in range(9):
                for j in range(9):
                    if b[i][j] == '.':
                        lst1 = b[i]
                        lst2 = [b[k][j] for k in range(9)]
                        lst3 = []
                        for p in range(i//3*3, i//3*3+3):
                            for q in range(j//3*3, j//3*3+3):
                                lst3.append(b[p][q])
                        for k in range(1, 10):
                            k = str(k)
                            if k not in lst1 and k not in lst2 \
                            and k not in lst3:
                                b[i][j] = k
                                if helper(b):
                                    return True
                                else: # Notice this is essential
                                    b[i][j] = '.'
                        return False

            return True

        helper(board)


