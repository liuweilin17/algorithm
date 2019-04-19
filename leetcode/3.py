###########################################
# Let's Have Some Fun
# File Name: 3.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Mar 29 15:04:58 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#3. Longest Substring Without Repeating Characters

import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dt = collections.defaultdict(int)
        N = len(s)
        if not N: return 0
        i = 0
        ret = 0
        for j in range(N):
            if not dt[s[j]]:
                ret = max(ret, j-i+1)
                dt[s[j]] = 1
            else:
                while s[i] != s[j]:
                    dt[s[i]] = 0
                    i+=1
                i+=1
        return ret





