###########################################
# Let's Have Some Fun
# File Name: 125.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Nov 23 14:10:33 2018
###########################################
#coding=utf-8
#!/usr/bin/python

#125. Valid Palindrome

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        i = 0
        j = l - 1
        while i < j:
            print(i)
            print(j)
            while (s[i].lower() < 'a' or s[i].lower()) > 'z' and (s[i] < '0' or s[i] > '9'):
                i += 1
                if i > l - 1: break
            while (s[j].lower() < 'a' or s[j].lower() > 'z') and (s[j] < '0' or s[j] > '9'):
                j -= 1
                if j < 0: break
            if i > l - 1 or j < 0:
                break
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True



if __name__ == '__main__':
    s = Solution()
    #print(s.isPalindrome("A man, a plan, a canal: Panama"))
    #print(s.isPalindrome("a."))
    #print(s.isPalindrome("OP"))
    print(s.isPalindrome("race a car"))

