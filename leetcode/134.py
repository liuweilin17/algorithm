###########################################
# Let's Have Some Fun
# File Name: 134.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Mar  4 22:55:56 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#134. Gas Station

class Solution:
    # brutal method
    def canCompleteCircuit1(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        candidates = []
        for i in range(N):
            if gas[i] >= cost[i]: candidates.append(i)
        #print(candidates)
        ret = -1
        for start in candidates:
            g, flag = 0, True
            for i in range(N):
                if g < 0:
                    flag = False
                    break
                ind = (start + i) % N
                #print('{}{}{}'.format(start, ind, g))
                g += (gas[ind] - cost[ind])
            if g >=0: return start
        return ret

    # total sum of gas[i]-cost[i] > 0, then possible
    # and the starts at next position of smallest subsums.
    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        total, sub_sum, start = 0, float('inf'), -1
        for i in range(N):
            total += (gas[i] - cost[i])
            if total < sub_sum:
                sub_sum = total
                start = i+1

        return -1 if total < 0 else start%N
