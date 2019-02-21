###########################################
# Let's Have Some Fun
# File Name: 524.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Feb 20 11:58:41 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#524. Longest Word in Dictionary through Deleting

# use two pointer to check the subsequence
class Solution:
    def findLongestWord(self, s: 'str', d: 'List[str]') -> 'str':
        d_sort = sorted(d, key=lambda x:(-len(x), x))

        m = len(s)
        for ss in d_sort:
            n = len(ss)
            i, j = 0, 0
            while i<m and j<n:
                if ss[j] != s[i]:
                    i += 1
                else:
                    i += 1
                    j += 1
            if j == n:
                return ss
        return ''


