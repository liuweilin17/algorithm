###########################################
# Let's Have Some Fun
# File Name: 19.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Feb 26 15:17:51 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#19. Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        q = head
        for i in range(n):
            q = q.next

        if q == None: return head.next # notice!!!
        else: q = q.next

        while q:
            q = q.next
            p = p.next
        t = p.next
        p.next = t.next
        del t
        return head
