###########################################
# Let's Have Some Fun
# File Name: 344.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Oct  4 12:19:50 2018
# Reverse String
###########################################
#coding=utf-8
#!/usr/bin/python

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = []
        l = len(s)
        for i in range(l):
            ret.append(s[l-i-1])
        return ''.join(ret)
    
    # This will result in Time limit Exception
    # Maybe due to the '+' operation between string
    # Next we should use list consisting of chars and then ''.join to combine a string!
    def reverseStringBad(self, s):
        ret = ''
        for i in s:
            ret = i + ret
        return ret

if __name__ == "__main__":
    s = Solution()
    print s.reverseString('hello')
    print s.reverseString('A man, a plan, a canal: Panama')

