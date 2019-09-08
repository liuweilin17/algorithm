###########################################
# Let's Have Some Fun
# File Name: 151.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Aug 26 22:38:31 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 151. Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        N = len(s)
        ret = []
        t = ''
        for i in range(N-1, -1, -1):
            if s[i] != ' ':
                t = s[i] + t
            elif t != '':
                ret.append(t)
                t = ''
            else: pass

        if t:
            ret.append(t)

        return ' '.join(ret)



