###########################################
# Let's Have Some Fun
# File Name: 445.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Mar 21 19:16:27 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#445. Add Two Numbers II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = 0
        while l1:
            a = a * 10 + l1.val
            l1 = l1.next
        b = 0
        while l2:
            b = b * 10 + l2.val
            l2 = l2.next

        c = a + b
        if c == 0: return ListNode(0)
        head = None
        while c:
            tnd = ListNode(c % 10)
            tnd.next = head
            head = tnd
            c //= 10

        return head

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        st1, st2 = [], []
        while l1:
            st1.append(l1.val)
            l1 = l1.next
        while l2:
            st2.append(l2.val)
            l2 = l2.next
        
        b = 0
        head = None
        while st1 and st2:
            x, y = st1.pop(), st2.pop()
            a = (x + y + b) % 10
            b = (x + y + b) // 10
            tmp = ListNode(a)
            tmp.next = head
            head = tmp
        st = []
        if st1: st = st1
        if st2: st = st2
        while st:
            t = st.pop()
            a = (t + b) % 10
            b = (t + b) // 10
            tmp = ListNode(a)
            tmp.next = head
            head = tmp
        
        if b:
            tmp = ListNode(b)
            tmp.next = head
            head = tmp
            
        return head

    def addTwoNumbers3(self, l1: ListNode, l2: ListNode) -> ListNode:
        st1 = []
        st2 = []
        while l1:
            st1.append(l1.val)
            l1 = l1.next
        while l2:
            st2.append(l2.val)
            l2 = l2.next
        remain = 0
        head = None # add before head
        while st1 or st2:
            a = st1.pop() if st1 else 0
            b = st2.pop() if st2 else 0
            sumV = remain + a + b
            nd = ListNode(sumV % 10)
            if not head: head = nd
            else:
                nd.next = head
                head = nd
            remain = sumV // 10
        if remain:
            nd = ListNode(remain)
            nd.next = head
            head = nd
        
        return head
