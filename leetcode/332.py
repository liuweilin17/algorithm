###########################################
# Let's Have Some Fun
# File Name: 332.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Sep  6 22:11:43 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#332. Reconstruct Itinerary

class Solution:
    # my solution, accepted but slow
    def findItinerary1(self, tickets: List[List[str]]) -> List[str]:
        self.ret = None
        g = collections.defaultdict(list)
        n = 0
        for begin, end in tickets:
            g[begin].append(end)
            n += 1

        for key in g:
            g[key].sort()

        def helper(start, path, gg, n):
            if sum([len(gg[key]) for key in gg]) == 0:
                self.ret = path[:]
                return True
            flag = False
            for nd in gg[start]:
                gg[start].remove(nd)
                if helper(nd, path+[nd], gg, n):
                    flag = True
                    break
                gg[start].append(nd)
                gg[start].sort()
            return flag

        helper("JFK", ["JFK"], g, n)
        return self.ret
