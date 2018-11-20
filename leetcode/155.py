###########################################
# Let's Have Some Fun
# File Name: 155.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Nov 20 12:47:18 2018
###########################################
#coding=utf-8
#!/usr/bin/python
# 155. Min Stack

class MinStack:
    '''
    use two stack
    stack1: all the current elements
    stack2: the mininum element of history
    '''
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        self.size1 = 0
        self.size2 = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.s1.append(x)
        if self.size2 > 0:
            minV, minInd = self.s2[self.size2-1]
            if x <= minV:
                self.s2.append((x, self.size1))
                self.size2 += 1
        else:
            self.s2.append((x, self.size1))
            self.size2 += 1
        self.size1 += 1

    def pop(self):
        """
        :rtype: void
        """
        if self.size1 <= 0:
            return None
        if self.size2 > 0:
            minV, minInd = self.s2[self.size2-1]
            if minV == self.s1[self.size1-1] and minInd == self.size1 - 1:
                self.s2.pop()
                self.size2 -= 1
        self.s1.pop()
        self.size1 -= 1

    def top(self):
        """
        :rtype: int
        """
        if self.size1 <= 0:
            return None
        else:
            return self.s1[self.size1-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.size2 > 0:
            return self.s2[self.size2-1][0]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.size1)
    print(obj.size2)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())


