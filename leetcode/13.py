###########################################
# Let's Have Some Fun
# File Name: 13.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Oct 12 18:48:42 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 13. Roman to Integer

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dt1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
                'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        dt2 = {'I':['V', 'X'], 'X':['L', 'C'], 'C':['D', 'M']}
        
        i = 0
        l = len(s)
        ret = 0
        while(i<l):
            if i<l-1 and s[i] in dt2.keys() and s[i+1] in dt2[s[i]]:
                ret += dt1[s[i]+s[i+1]]
                i += 1
            else:
                ret += dt1[s[i]]
            i += 1
        return ret

if __name__ == '__main__':
    s = Solution()
    print s.romanToInt("III")
    print s.romanToInt("IV")
    print s.romanToInt("IX")
    print s.romanToInt("LVIII")
    print s.romanToInt("MCMXCIV")
