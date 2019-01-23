###########################################
# Let's Have Some Fun
# File Name: 142.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Jan 22 10:51:25 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 142. Linked List Cycle II
# we use Floyd's Tortoise and Hare (Cycle Detection) to detect
# see reference
# https://cs.stackexchange.com/questions/10360/floyds-cycle-detection-algorithm-determining-the-starting-point-of-cycle

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # O(n**2)
    def detectCycle1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        p = head
        s = set()
        while True:
            if not p:
                return None
            if p in s:
                return p
            s.add(p)
            p = p.next
    
    # O(n)
    def detectCycle2(self, head):
        if not head: return None

        fastPtr = head
        slowPtr = head
        meetPtr = None
        flag = 1
        while True:
            if fastPtr == slowPtr and not flag:
                meetPtr = fastPtr
                break
            if fastPtr and fastPtr.next and slowPtr:
                fastPtr = fastPtr.next.next
                slowPtr = slowPtr.next
            else:
                return None
            flag = 0

        p = head
        q = meetPtr
        while True:
            if p == q:
                return p
            p = p.next
            q = q.next
