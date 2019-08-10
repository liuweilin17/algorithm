###########################################
# Let's Have Some Fun
# File Name: 9.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat  6 Jul 11:58:41 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x % 10 != 0 is essential
        if x < 0 or (x%10 == 0 and x != 0): return False

        reverse = 0

        while x>reverse:
            reverse = reverse*10 + x%10
            x //= 10

        # x == reverse, even number
        # x == reverse/10, odd number
        print(x, reverse)
        return x == reverse or x == reverse // 10

