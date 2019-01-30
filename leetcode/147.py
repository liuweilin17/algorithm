###########################################
# Let's Have Some Fun
# File Name: 147.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Jan 29 00:43:14 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#147. Insertion Sort List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        
        h1 = head # the head of sorted linked list
        h2 = head.next # the head of unsorted linked list
        h1.next = None
        
        while h2:
            bak = h2.next
            
            # insert h2 into h1
            h2.next = None
            cur, pre = h1, None
            while cur:
                if cur.val < h2.val:
                    pre = cur
                    cur = cur.next
                else: break
            if pre: # add h2 after pre
                q = pre.next
                pre.next = h2
                h2.next = q
            else: # add h2 to the front
                h2.next = h1
                h1 = h2
                
            h2 = bak
        
        return h1
        

