###########################################
# Let's Have Some Fun
# File Name: 21.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Nov  9 11:08:07 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val < l2.val:
            l3_head = l1
            l1 = l1.next
        else:
            l3_head = l2
            l2 = l2.next
        l3_head.next = None
        l3_tail = l3_head

        while l1 != None and l2!= None:
            if l1.val < l2.val:
                tmp = l1
                l1 = l1.next
            else:
                tmp = l2
                l2 = l2.next
            tmp.next = None
            l3_tail.next = tmp
            l3_tail = tmp
        if l1 != None:
            l3_tail.next = l1
        if l2 != None:
            l3_tail.next = l2
        return l3_head

if __name__ == '__main__':
    n11 = ListNode(1)
    n12 = ListNode(2)
    n13 = ListNode(4)
    n12.next = n13
    n11.next = n12
    n21 = ListNode(1)
    n22 = ListNode(3)
    n23 = ListNode(4)
    n22.next = n23
    n21.next = n22
    
    s = Solution()
    n3 = s.mergeTwoLists(n11,n21)
    while(n3):
        print n3.val
        n3 = n3.next


