###########################################
# Let's Have Some Fun
# File Name: 844.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Apr  9 23:44:30 2020
###########################################
#coding=utf-8
#!/usr/bin/python

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # stack, O(N) space, O(N) time
        def helper(s):
            st = []
            for c in s:
                if c != '#':
                    st.append(c)
                elif st:
                    st.pop()
                else: pass
            return ''.join(st)

        return helper(S) == helper(T)

    def backspaceCompare(self, S: str, T: str) -> bool:
        N, M = len(S), len(T)
        if not N and not M: return True
        i, j = N-1, M-1
        while i >= 0 or j >= 0: # Notice 'or', when S finished, T could also be empty string
            skip = 0
            while i >= 0:
                if S[i] == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else: break
                i -= 1
            skip = 0
            while j >= 0:
                if T[j] == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else: break
                j -= 1

            a = S[i] if i >= 0 else ''
            b = T[j] if j >= 0 else ''
            if a != b: return False
            i -= 1
            j -= 1

        return True
