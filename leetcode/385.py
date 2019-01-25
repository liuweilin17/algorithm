###########################################
# Let's Have Some Fun
# File Name: 385.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Jan 24 18:21:38 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 385. Mini Parser

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# In this question, we simply need to clarify the different conditions.
# traverse the string
# when '[' encountered, add to stack
# when number encountered, try to add to stack
# when ']' encountered, pop stack until '[' is poped, we create a nestedinteger with these 
# poped nestedinteger and add it to stack. Notice, we to reverse the ordered of poped nestedinteger.
# The final element in stack is what we want.
class Solution:
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        st = []
        num = 0
        flag = 0 # 0: no current number, 1: current number is positive, -1: current number is negative
        n = len(s)
        for i in range(n):
            c = s[i]
            if c == '[': #append and add current number
                if flag != 0:
                    st.append(NestedInteger(num * flag))
                    flag = 0
                    num = 0
                st.append(c)
            elif c >= '0' and c <= '9': #calculate current number
                num = num * 10 + int(c)
                if flag == 0: flag = 1
                if i == n-1: # if there is only one integer in the string, we simply add it to the stack
                    st.append(NestedInteger(num*flag))
            elif c == '-': # negative
                flag = -1
                num = 0
            elif c == ',': # if there is current number, then add it.
                if flag != 0:
                    st.append(NestedInteger(num * flag))
                    flag = 0
                    num = 0
            else: # ']'
                if flag != 0: # if there is current number, then add it.
                    st.append(NestedInteger(num * flag))
                    flag = 0
                    num = 0
                tmp = st.pop()
                lst = []
                while tmp != '[': # pop until '[' is encountered.
                    lst.append(tmp)
                    tmp = st.pop()
                nst = NestedInteger()
                for nl in lst[::-1]: # reverse the order of poped, and create a new nestedinteger.
                    nst.add(nl)
                st.append(nst)

        return st[0]
