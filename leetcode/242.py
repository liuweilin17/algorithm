###########################################
# Let's Have Some Fun
# File Name: 242.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Oct 19 00:40:47 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# valid anagram

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dt = {}
        l1 = len(s)
        l2 = len(t)
        if l1 != l2:
            return False
        for c in s:
            if c in dt.keys():
                dt[c] += 1
            else:
                dt[c] = 1
        for c in t:
            if c in dt.keys():
                dt[c] -= 1
                if dt[c] < 0:
                    return False
            else:
                return False
        return True


if __name__ == '__main__':
    so = Solution()
    s = "anagram"
    t = "nagaram"
    print so.isAnagram(s, t)
    s = "rat"
    t = "car"
    print so.isAnagram(s, t)
