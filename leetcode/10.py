###########################################
# Let's Have Some Fun
# File Name: 10.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Sep 15 12:31:56 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 10. Regular Expression Matching

class Solution:
    # recursion
    def isMatch(self, s: str, p: str) -> bool:
        M = len(s)
        N = len(p)
        if M == 0 and N == 0:
            return True
        elif M != 0 and N == 0:
            return False
        elif N == 1:
            return len(s) == 1 and (p[0] == s[0] or p[0] == '.')
        else: pass

        cur = p[0]
        nst = p[1]
        if nst != '*':
            if not s or (cur != s[0] and cur != '.'):
                return False
            else:
                return self.isMatch(s[1:], p[1:])
        else:
            i = 0 # position in s
            if cur == '.':
                flag = False
                while i <= M:
                    flag = self.isMatch(s[i:], p[2:])
                    if flag: break
                    i += 1
                return flag
            else:
                flag = self.isMatch(s, p[2:])
                if flag:
                    return True
                i = 0
                while i < M and s[i] == cur:
                    flag = self.isMatch(s[i+1:], p[2:])
                    if flag:
                        return True
                    i += 1
                return flag
    
    # recursion with DP
    def isMatch(self, s: str, p: str) -> bool:
        M = len(s)
        N = len(p)
        # dp[i][j]: isMatch of s[i:] and p[j:]
        # 0: unkown, 1:True, -1:False
        dp = [[0 for i in range(N+1)] for _ in range(M+1)]
        for i in range(M+1):
            dp[i][N] = -1
        dp[M][N] = 1

        def helper(s, p, i, j, M, N):
            if dp[i][j] != 0:
                print(i, j, s[i:], p[j:], 'are used !!')
                return True if dp[i][j] == 1 else False
            if j == N-1:
                dp[i][j] = i == M-1 and (s[i] == p[j] or p[j] == '.')
                return dp[i][j]
            else:
                cur, nst = p[j], p[j+1]
                if nst != '*':
                    if i == M or (cur != s[i] and cur != '.'):
                        return False
                    else:
                        return helper(s, p, i+1, j+1, M, N)
                else:
                    k = i
                    if cur == '.':
                        flag = False
                        while k <= M:
                            flag = helper(s, p, k, j+2, M, N)
                            if flag: break
                            k += 1
                        dp[i][j] = flag
                        return flag
                    else:
                        flag = helper(s, p, i, j+2, M, N)
                        if flag:
                            dp[i][j] = flag
                            return True
                        k = i
                        while k < M and s[k] == cur:
                            flag = helper(s, p, k+1, j+2, M, N)
                            if flag:
                                dp[i][j] = flag
                                return True
                            k += 1
                        dp[i][j] = False
                        return False

        return helper(s, p, 0, 0, M, N)
