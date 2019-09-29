###########################################
# Let's Have Some Fun
# File Name: 65.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Sep 25 12:01:42 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#65. Valid Number

class Solution:
    def isNumber(self, s: str) -> bool:

        def checkValid(s, is_float):
            # check if s is valid (s does not contain e)
            # is_float: whether a float number is allowed
            if not len(s): return False
            if s[0] == '-' or s[0] == '+':
                s = s[1:]
            if not len(s): return False
            dot_flag = False
            N = len(s)
            for i in range(N):
                c = s[i]
                if c == '.':
                    if is_float:
                        if dot_flag: return False
                        # elif i == 0 or i == N-1: return False
                        else: dot_flag = True
                    else:
                        return False
                elif not c.isdigit():
                    return False
                else: pass
            return True if s != '.' else False

        s = s.strip(' ')
        arr = s.split('e')
        N = len(arr)
        if N == 1:
            return checkValid(s, True)
        elif N == 2: # handle e number
            # handle arr[0]
            return checkValid(arr[0], True) and checkValid(arr[1], False)
        else:
            return False

