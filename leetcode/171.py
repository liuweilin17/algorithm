###########################################
# Let's Have Some Fun
# File Name: 171.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Oct 12 16:55:45 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 171. Excel Sheet Column Number

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        l = len(s)
        for i in range(l):
            # ord(): get the ascii value of character
            tmp = ord(s[i]) - ord('A') + 1
            res = res * 26 + tmp
        return res

if __name__ == '__main__':
    s = Solution()
    print s.titleToNumber('A')
    print s.titleToNumber('AB')
    print s.titleToNumber('ZY') 
