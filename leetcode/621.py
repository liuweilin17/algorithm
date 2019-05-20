###########################################
# Let's Have Some Fun
# File Name: 621.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat May 18 16:46:59 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#621. Task Scheduler

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        N = len(tasks)
        if not N: return 0
        if n == 0: return len(tasks)

        dt = collections.Counter(tasks)
        tasks_uniq = list(dt.keys())
        tasks_uniq.sort(key=lambda x:dt[x], reverse=True)
        M = len(tasks_uniq)

        days = 0
        while dt[tasks_uniq[0]] > 0:
            for i in range(n + 1):
                if dt[tasks_uniq[0]] == 0:
                    break
                if i<M and dt[tasks_uniq[i]] > 0:
                    dt[tasks_uniq[i]] -= 1
                days += 1

            tasks_uniq.sort(key=lambda x: dt[x], reverse=True)

        return days


