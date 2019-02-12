###########################################
# Let's Have Some Fun
# File Name: 131.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Feb 11 17:19:17 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#131. Palindrome Partitioning

class Solution:
    def partition(self, s: 'str') -> 'List[List[str]]':
        ret = []

        def backtrack(s, path):
            # s is the unpartitioned part
            # path is the array of Palindrome
            if s == '':
                ret.append(path[:])
            for i in range(len(s)):
                tmp = s[i:]
                if tmp == tmp[::-1]:
                    backtrack(s[:i], [tmp[:]]+path)
        backtrack(s, [])
        return ret



