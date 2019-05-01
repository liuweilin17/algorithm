###########################################
# Let's Have Some Fun
# File Name: 138.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Apr 28 20:34:36 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#138. Copy List with Random Pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dt = {}

        head_new = Node(0, None, None)
        p1 = head_new
        p2 = head
        while p2:
            val = p2.val
            random = p2.random
            p1.next = Node(val, None, random)
            dt[p2] = p1.next
            p1 = p1.next
            p2 = p2.next

        head_new = head_new.next
        p = head_new
        while p:
            if p.random:
                p.random = dt[p.random]
            p = p.next

        return head_new


