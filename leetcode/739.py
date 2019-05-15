###########################################
# Let's Have Some Fun
# File Name: 739.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue 14 May 10:50:32 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#739. Daily Temperatures

class Solution:
    # time: O(NW), space: O(N+W)
    def dailyTemperatures1(self, T: List[int]) -> List[int]:
        N = len(T)
        if not T: return []

        ret = [0] * N
        pos_dict = {}
        for i in range(N-1, -1, -1):
            t = T[i]
            pos_dict[t] = i # the first position appears after i
            pos = N+1
            for j in range(t+1, 101):
                if j in pos_dict:
                    pos = min(pos_dict[j], pos)
            if pos != N+1:
                ret[i] = pos - i

        return ret

    # time: O(N), space: O(N)
    def dailyTemperatures2(self, T: List[int]) -> List[int]:
        N = len(T)
        if not T: return []
        
        # stack[i]: position of last higher temperature, stack[-1] < stack[-2]
        stack = []
        ret = [0] * N
        for i in range(N-1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack: ret[i] = stack[-1] - i
            stack.append(i)
            
        return ret



