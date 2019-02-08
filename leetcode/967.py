###########################################
# Let's Have Some Fun
# File Name: 967.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Dec 30 09:50:53 2018
###########################################
#coding=utf-8
#!/usr/bin/python
class Solution:
    # recursive
    def numsSameConsecDiff1(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1: return list(range(10))
        ret = []

        dt = {}
        for i in range(10):
            tmp = []
            if i+K < 10: tmp.append(i+K)
            if i-K > -1: tmp.append(i-K)
            dt[i] = tmp

        ret1 = self.numsSameConsecDiff1(N-1, K)
        for i in ret1:
            if i==0: continue
            j = i % 10
            if j + K < 10: ret.append(i*10 + j + K)
            if K!=0 and j - K > -1: ret.append(i*10 + j - K)
        return ret

    # iterative
    def numsSameConsecDiff2(self, N, K):
        ans = {x for x in range(1, 10)}
        for _ in xrange(N-1):
            ans2 = set()
            for x in ans:
                d = x % 10
                if d - K >= 0:
                    ans2.add(10*x + d-K)
                if d + K <= 9:
                    ans2.add(10*x + d+K)
            ans = ans2

        if N == 1:
            ans.add(0)

        return list(ans)
