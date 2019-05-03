###########################################
# Let's Have Some Fun
# File Name: 433.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu May  2 12:05:40 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#433. Minimum Genetic Mutation

from queue import Queue

class Solution:
    # quite similar to question 127. Word Ladder
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not start or not end or end not in bank or not bank: return -1

        # create intermediate dict
        dt = collections.defaultdict(list)
        N = len(start)
        for word in bank:
            for i in range(N):
                dt[word[:i] + '*' + word[i+1:]].append(word)

        # bfs
        seen = [start]
        Q = Queue()
        Q.put((start, 0))
        while not Q.empty():
            word, level = Q.get()
            for i in range(N):
                intermediate = word[:i]+'*'+word[i+1:]
                for wordd in dt[intermediate]:
                    if wordd == end:
                        return level + 1
                    elif wordd not in seen:
                        Q.put((wordd, level+1))
                        seen.append(wordd)
                dt[intermediate] = []

        return -1


