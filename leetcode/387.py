###########################################
# Let's Have Some Fun
# File Name: 387.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Oct 19 11:08:28 2018
###########################################
#coding=utf-8
#!/usr/bin/python

#387. First Unique Character in a String

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dt = {}
        l = len(s)
        for i in range(l):
            c = s[i]
            if c in dt.keys():
                dt[c] = l
            else:
                dt[c] = i
        min_p = l
        for c in dt.keys():
            if dt[c] < min_p:
               min_p = dt[c]
        if min_p == l:
            return -1
        else:
            return min_p

if __name__ == '__main__':
    so = Solution() 
    s = "leetcode"
    print so.firstUniqChar(s)
    s = "loveleetcode"
    print so.firstUniqChar(s)
