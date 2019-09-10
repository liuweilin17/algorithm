###########################################
# Let's Have Some Fun
# File Name: 318.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Sep  6 08:53:07 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#318. Maximum Product of Word Lengths

class Solution:
    # AC, but not efficient enough
    def maxProduct1(self, words: List[str]) -> int:
        lst = []
        for word in words:
            t = [0] * 26
            for char in word:
                t[ord(char)-ord('a')] = 1
            lst.append(t[:])

        N = len(words)
        ret = 0
        for i in range(N):
            for j in range(i+1, N):
                tmp = len(words[i]) * len(words[j])
                if tmp <= ret: continue
                flag = False
                for k in range(26):
                    if lst[i][k] == 1 and lst[j][k] == 1:
                        flag = True
                        break
                if not flag:
                    ret = tmp

        return ret
   
   # use list to store the value, faster
    def maxProduct2(self, words: List[str]) -> int:
        N = len(words)
        lst = [0] * N
        for i in range(N):
            word = words[i]
            tmp = 0
            for char in word:
                tmp |= 1 << (ord(char)-ord('a'))
            lst[i] = tmp

        ret = 0
        for i in range(N):
            for j in range(i+1, N):
                tmp = len(words[i]) * len(words[j])
                if tmp <= ret: continue
                elif lst[i] & lst[j] > 0: continue
                else: ret = tmp

        return ret
   
   # use dict to store the value, fastest
    def maxProduct3(self, words: List[str]) -> int:
        N = len(words)
        dt = {} # mask: length of original word
        for i in range(N):
            word = words[i]
            tmp = 0
            for char in set(word):
                tmp |= 1 << (ord(char)-ord('a'))
            dt[tmp] = max(dt.get(tmp, 0), len(word))
            
        ret = 0
        for x in dt:
            for y in dt:
                if not x & y:
                    ret = max(ret, dt[x]*dt[y])
                    
        return ret
        
