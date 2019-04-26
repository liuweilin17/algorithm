###########################################
# Let's Have Some Fun
# File Name: 516.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Apr 22 20:35:00 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#516. Longest Palindromic Subsequence

class Solution:
    # time limit exceed
    def longestPalindromeSubseq1(self, s: str) -> int:
        if len(s) <= 1: return len(s)

        if s[0] == s[-1]:
            return self.longestPalindromeSubseq(s[1:-1]) + 2
        else:
            return max(self.longestPalindromeSubseq(s[1:]), self.longestPalindromeSubseq(s[:-1]))
   
   def longestPalindromeSubseq2(self, s: str) -> int:
        N = len(s)
        dp = [N * [-1] for i in range(N)]
        left, right = 0, len(s)-1
        
        def helper(s, left, right):
            if left > right:
                return 0
            if left == right:
                return 1
            if dp[left][right] != -1: return dp[left][right]
            if s[left] == s[right]:
                dp[left][right] = helper(s, left+1, right-1) + 2
                return dp[left][right]
            else:
                dp[left][right] = max(helper(s, left+1, right), helper(s, left, right-1))
                return dp[left][right]
        
        return helper(s, left, right) 
