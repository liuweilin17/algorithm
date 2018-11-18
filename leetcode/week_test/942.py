###########################################
# Let's Have Some Fun
# File Name: 942.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Nov 18 11:08:45 2018
###########################################
#coding=utf-8
#!/usr/bin/python

#942. DI String Match

class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        l = len(S) + 1
        a = [0] * l # result array
        for i in range(1, l):
            if S[i-1] == 'I':
                a[i] = a[i-1] + 1
            else:
                a[i] = a[i-1] - 1
        b = sorted(a) # sort
        c = range(l) # candidate numbers
        dt = {}
        for i in range(l):
            if b[i] in dt.keys():
                dt[b[i]].append(c[i])
            else:
                dt[b[i]] = [c[i]]
        for i in range(l):
            a[i] = dt[a[i]].pop()
        return a

