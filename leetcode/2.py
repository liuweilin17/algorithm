###########################################
# Let's Have Some Fun
# File Name: 2.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Mar 21 18:40:59 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        p = head
        b = 0
        while l1 and l2:
            a = (l1.val + l2.val + b) % 10
            b = (l1.val + l2.val + b) // 10
            tmp = ListNode(a)
            p.next = tmp
            p = p.next
            l1 = l1.next
            l2 = l2.next

        q = None
        if l1:
            q = l1
        if l2:
            q = l2
        while q:
            a = (q.val + b) % 10
            b = (q.val + b) // 10
            tmp = ListNode(a)
            p.next = tmp
            p = p.next
            q = q.next
        if b != 0:
            p.next = ListNode(b)

        return head.next
    
    # neat version
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        remain = 0
        head = ListNode(0)
        p = head
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            sumV = remain + a + b
            p.next = ListNode(sumV % 10)
            p = p.next
            remain = sumV // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if remain:
            p.next = ListNode(remain)

        return head.next
