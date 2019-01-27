###########################################
# Let's Have Some Fun
# File Name: 438.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Jan 26 11:12:04 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 438. Find All Anagrams in a String

class Solution:
    # O((n-m)mlogm)
    def findAnagrams1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ret = []
        m = len(p)
        n = len(s)
        sorted_p = sorted(p)
        if m > n: return []
        for i in range(n - m + 1):
            if sorted(s[i:i + m]) == sorted_p:
                ret.append(i)
        return ret

    # O(n), much faster
    def findAnagrams2(self, s, p):
        ret = []
        m = len(p)
        n = len(s)
        if m > n: return []

        countP = [0] * 26
        for c in p:
            countP[ord(c) - ord('a')] += 1

        countS = [0] * 26
        for i in range(m):
            countS[ord(s[i]) - ord('a')] += 1

        for i in range(m, n):
            if countS == countP: ret.append(i - m)
            countS[ord(s[i - m]) - ord('a')] -= 1
            countS[ord(s[i]) - ord('a')] += 1
        if countS == countP: ret.append(n - m)

        return ret





