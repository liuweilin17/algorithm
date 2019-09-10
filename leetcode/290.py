###########################################
# Let's Have Some Fun
# File Name: 290.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Sep  4 09:49:03 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#290. Word Pattern

class Solution:
    def wordPattern1(self, pattern: str, str: str) -> bool:
        N1 = len(pattern)
        str_arr = str.split(" ")
        N2 = len(str_arr)
        if N1 != N2: return False

        dt1, dt2 = {}, {}
        for i in range(N1):
            p, s = pattern[i], str_arr[i]
            if p in dt1:
                if dt1[p] != s:
                    return False
            elif s in dt2:
                if dt2[s] != p:
                    return False
            else:
                dt1[p] = s
                dt2[s] = p


        return True

    def wordPattern2(self, pattern: str, str: str) -> bool:
        s_arr = str.split(' ')
        return list(map(pattern.find, pattern)) == list(map(s_arr.index, s_arr))
        

