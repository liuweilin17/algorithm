###########################################
# Let's Have Some Fun
# File Name: 87.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Oct 12 12:39:39 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#87. Scramble String

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        N1, N2 = len(s1), len(s2)
        if N1 != N2 or sorted(s1) != sorted(s2):
            return False
        elif N1 < 4 or s1 == s2:
            return True
        else:
            for i in range(1, N1):
                if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                    return True
            return False
        
