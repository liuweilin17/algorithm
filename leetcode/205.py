###########################################
# Let's Have Some Fun
# File Name: 205.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu 29 Aug 11:47:36 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dt, dt_rev = {}, {}
        N1, N2 = len(s), len(t)
        if N1 != N2: return False

        for i in range(N1):
            c1, c2 = s[i], t[i]
            if c1 not in dt:
                if c2 not in dt_rev:
                    dt[c1] = c2
                    dt_rev[c2] = c1
                else:
                    if dt_rev[c2] != c1:
                        return False
            else:
                if dt[c1] != c2: return False

        return True

