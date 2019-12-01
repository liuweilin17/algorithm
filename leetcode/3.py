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

    def lengthOfLongestSubstring2(self, s: str) -> int:
        dt = {} # the first appearing index of c
        left, right = 0, 0
        N = len(s)
        maxL = 0
        while left <= right and right < N:
            c = s[right]
            if c not in dt:
                dt[c] = right
            else:
                maxL = max(maxL, right-left)
                pre = dt[c]
                # clear all records of c before pre
                for i in range(left, pre+1):
                    del dt[s[i]]
                left = pre + 1
                dt[c] = right
            right += 1
        # print(left)
        maxL = max(right-left, maxL)
        return maxL





