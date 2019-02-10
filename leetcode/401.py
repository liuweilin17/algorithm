###########################################
# Let's Have Some Fun
# File Name: 401.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Feb  9 12:17:51 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#401. Binary Watch

class Solution:
    def readBinaryWatch(self, num: 'int') -> 'List[str]':
        
        def backtrack(num, tmp, ret, t): 
            # notice!!! t is important, else it will be time limit exceed
            # this is actually the use of combinations
            if num == 0:
                h = sum([2**i if tmp[i] == 1 else 0 for i in range(4)]) 
                m = sum([2**(i-4) if tmp[i] == 1 else 0 for i in range(4,10)])
                if h <= 11 and m <= 59:
                    if m<10:
                        ret.append(str(h)+':0'+str(m))
                    else:
                        ret.append(str(h)+':'+str(m))
            else:
                for i in range(t, 10):
                    if tmp[i] == 0:
                        bak = tmp[:]
                        bak[i] = 1
                        backtrack(num-1, bak[:], ret, i+1)
                        
        if num < 0: return []
        ret = []
        tmp = [0] * 10
        backtrack(num, tmp, ret, 0)
        return list(set(ret))
        
