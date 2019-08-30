###########################################
# Let's Have Some Fun
# File Name: 143.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri 23 Aug 13:30:04 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#143. Reorder List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList1(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        count = 0
        st = []
        p = head
        while p:
            st.append(p)
            p = p.next
            count += 1

        ret = ListNode(-1)
        r = ret
        N = count // 2
        for i in range(N):
            nd1 = st[i]
            nd1.next = None
            r.next = nd1
            r = r.next
            nd2 = st[-i-1]
            nd2.next = None
            r.next = nd2
            r = r.next

        if count % 2:
            nd = st[N]
            nd.next = None
            r.next = nd


        return ret.next

    def reorderList2(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return head

        # find the middle points (p)
        p = head
        q = head
        while p and q and q.next:
            p = p.next
            q = q.next.next
        q = p.next
        p.next = None

        # reverse the second list (q)
        head2 = None
        while q:
            bak = q.next
            q.next = head2
            head2 = q
            q = bak

        # merge two lists (head and head2)
        p, q = head, head2
        ret = ListNode(0)
        r = ret
        while p or q:
            bak1 = p.next if p else None
            bak2 = q.next if q else None
            if p:
                r.next = p
                r = r.next
                r.next = None
            if q:
                r.next = q
                r = r.next
                r.next = None
            p, q = bak1, bak2

        return ret.next


