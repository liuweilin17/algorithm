###########################################
# Let's Have Some Fun
# File Name: 22.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Jan 11 09:27:46 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 22. Generate Parentheses

class Solution:
    # brutal method, similar to 17
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(A):
            if len(A) == 2*n:
                if valid(A):
                    ret.append(''.join(A))
                    print(''.join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for i in A:
                if i == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0

        ret = []
        A = []
        generate(A)
        return ret

    # backtracking
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        def backtrack(A='', left = 0, right = 0):
            if len(A) == 2*n:
                ret.append(A)
            if left < n:
                backtrack(A+'(', left+1, right)
            if right < left:
                backtrack(A+')', left, right+1)
        backtrack()
        return ret
