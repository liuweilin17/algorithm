###########################################
# Let's Have Some Fun
# File Name: 299.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Sep  4 10:59:43 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#299. Bulls and Cows

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        dt1, dt2 = collections.Counter(secret), collections.Counter(guess)
        N = len(secret)
        for i in range(N):
            if secret[i] == guess[i]:
                bulls += 1

        for e in dt1:
            if e in dt2:
                cows += min(dt1[e], dt2[e])
        cows -= bulls # cows could be calculated like this !!!

        return str(bulls)+'A'+str(cows)+'B'
