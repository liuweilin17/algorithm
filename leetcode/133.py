###########################################
# Let's Have Some Fun
# File Name: 133.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Apr 29 19:39:00 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 133. Clone Graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from queue import Queue
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        seen = []
        nodes = []
        dt = {}
        q = Queue()
        q.put(node)
        # clone all the nodes, neighbors stay the same
        while not q.empty():
            nd = q.get()
            if nd not in seen:
                new_nd = Node(nd.val, nd.neighbors)
                nodes.append(new_nd)
                seen.append(nd)
                dt[nd] = new_nd
                for ndd in nd.neighbors:
                    q.put(ndd)

        # traverse all the nodes, replace neighbors with new ones
        for nd in nodes:
            new_neighbors = []
            for ndd in nd.neighbors:
                new_neighbors.append(dt[ndd])
            nd.neighbors = new_neighbors

        return dt[node]


