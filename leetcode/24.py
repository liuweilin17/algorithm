###########################################
# Let's Have Some Fun
# File Name: 24.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun  7 Jul 20:09:25 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#24. Swap Nodes in Pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ret = ListNode(0)
        ret.next = head

        p = ret
        while p and p.next and p.next.next:
            q = p.next
            r = q.next
            p.next = r
            q.next = r.next
            r.next = q # Notice update r in the last step
            p = q
        return ret.next
