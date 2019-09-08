###########################################
# Let's Have Some Fun
# File Name: 1177.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Sep  1 09:28:50 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 1177. Can Make Palindrome from Substring

import collections

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        # cummutive count of letters could reduce the time conplexity
        cnt = []
        dt = [0 for i in range(26)]
        for c in s:
            cnt.append(dt[:])
            dt[ord(c) - ord('a')] += 1
        cnt.append(dt[:])
        print(cnt)
        
        ret = []
        for left, right, k in queries:
            num_odds = sum([(b-a)&1 for a, b in zip(cnt[left], cnt[right+1])])
            ret.append(k >= num_odds // 2)
            
        return ret

