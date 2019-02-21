###########################################
# Let's Have Some Fun
# File Name: 692.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Feb 20 10:18:24 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#692. Top K Frequent Words

class Solution:
    # sort
    def topKFrequent1(self, words: 'List[str]', k: 'int') -> 'List[str]':
        dt = {}
        for word in words:
            dt[word] = dt.get(word, 0) + 1
        return sorted(dt.keys(), key = lambda x: (-dt[x], x))[:k]

    # heap
    def topKFrequent2(self, words: 'List[str]', k: 'int') -> 'List[str]':
        dt = {}
        for word in words:
            dt[word] = dt.get(word, 0) + 1
        return heapq.nsmallest(k, dt.keys(), key=lambda x:(-dt[x], x))
