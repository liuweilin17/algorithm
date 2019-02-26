###########################################
# Let's Have Some Fun
# File Name: 763.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Feb 24 11:59:55 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#763. Partition Labels

class Solution:
    def partitionLabels(self, S: 'str') -> 'List[int]':
        # count the last pos of each letter
        dt = {}
        N = len(S)
        for i in range(N):
            dt[S[i]] = i

        last = 0
        pre = 0
        ret = []
        for i in range(N):
            if dt[S[i]] > last:
                last = dt[S[i]]
            if i == last:
                ret.append(i-pre+1)
                last = i+1
                pre = i+1
        return ret



