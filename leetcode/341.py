###########################################
# Let's Have Some Fun
# File Name: 341.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Jan 24 14:42:46 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 341. Flatten Nested List Iterator

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
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

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = nestedList
        # we use a stack to store the unvisited integers of nestedList.
        self.st = []
        for i in range(len(nestedList)):
            t = nestedList[-i-1]
            self.st.append(t)

        #print(len(self.st))

    def next(self):
        """
        :rtype: int
        """
        if not len(self.st): return None

        tmp = self.st.pop()
        if tmp.isInteger():
            return tmp.getInteger()
        else:
            nlst = tmp.getList()
            for i in range(len(nlst)):
                t = nlst[-i-1]
                self.st.append(t)
            return self.next()

    # notice !!!
    # in this method, we have to consider a special kind case:
    # [[],[[]]], the result should be [] rather than [None]
    # we use hasNext() to get next, if all the next element is None, then it has no next.
    # otherwise, we insert NestedInteger(tmp) back to the stack.
    def hasNext(self):
        """
        :rtype: bool
        """
        #if len(self.st): return True
        #else: return False
        while len(self.st):
            tmp = self.next()
            if tmp or tmp == 0: #notice !!!
                self.st.append(NestedInteger(tmp))
                break
        if len(self.st): return True
        else: return False




# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
