###########################################
# Let's Have Some Fun
# File Name: 395.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Feb 11 22:13:21 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#395. Longest Substring with At Least K Repeating Characters

import re

class Solution:
    def longestSubstring(self, s: 'str', k: 'int') -> 'int':
        # splitting method, divide and conquer
        dt = {}
        for c in s:
            dt[c] = dt.get(c, 0) + 1
        t = []
        for c in dt.keys():
            if dt[c] < k:
                t.append(c)
        if not t:
            return len(s)
        else:
            s = re.split('|'.join(t), s)
            ret = 0
            for ss in s:
                if ss:
                    ret = max(ret, self.longestSubstring(ss, k))
            return ret

