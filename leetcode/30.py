###########################################
# Let's Have Some Fun
# File Name: 30.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Sep 16 22:03:46 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#30. Substring with Concatenation of All Words

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        N = len(s)
        M = len(words)
        if not s or not M: return []
        l = len(words[0])
        L = l * M
        dt = collections.Counter(words)
        ret = []
        for i in range(N-L+1):
            t = s[i:i+L]
            dt_tmp = {}
            flag = True
            for j in range(0, L-l+1, l):
                dt_tmp[t[j:j+l]] = dt_tmp.get(t[j:j+l], 0) + 1
                if dt_tmp[t[j:j+l]] > dt[t[j:j+l]]:
                    flag = False
                    break
            if flag and dt_tmp == dt:
                ret.append(i)

        return ret


