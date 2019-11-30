###########################################
# Let's Have Some Fun
# File Name: 1208.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Sep 29 11:59:35 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#1208. Get Equal Substrings Within Budget

class Solution:
    def equalSubstring1(self, s: str, t: str, maxCost: int) -> int:
        # two pointer
        N = len(s)
        left, right = 0, 0
        sumv = 0
        max_len = 0
        while left <= right and left < N:
            if sumv <= maxCost:
                if right < N:
                    sumv += abs(ord(s[right])-ord(t[right]))
                    right += 1
                else:
                    max_len = max(max_len, right-left)
                    left += 1
            else:
                max_len = max(max_len, right-left-1)
                sumv -= abs(ord(s[left])-ord(t[left]))
                left += 1

        return max_len

    def equalSubstring2(self, s: str, t: str, maxCost: int) -> int:
        N = len(s)
        if not s: return 0

        left, right = 0, 0
        max_len, tmp = 0, 0
        while right < N:
            cost = abs(ord(s[right]) - ord(t[right]))
            tmp += cost
            if tmp <= maxCost:
                max_len = max(max_len, right-left+1)
            else:
                while left <= right:
                    if tmp <= maxCost:
                        break
                    tmp -= abs(ord(s[left]) - ord(t[left]))
                    left += 1
            right += 1

        return max_len



