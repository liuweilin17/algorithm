#!/usr/bin/env python
# coding=utf-8
import Queue

class Node:
    "A Node in the Binary Tree"
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addLeft(self, N):
        self.left = N

    def addRight(self, N):
        self.right = N

    def breathFirstTraverse(self):
        if self == None:
            return
        q = Queue.Queue()
        q.put(self)
        while not q.empty():
            N_tmp = q.get()
            N_tmp.printNode()
            if N_tmp.left != None:
                q.put(N_tmp.left)
            if N_tmp.right != None:
                q.put(N_tmp.right)

    def preOrderTraverseRecur(self):
        if self != None:
            self.printNode()
        if self.left != None:
            self.left.preOrderTraverseRecur()
        if self.right != None:
            self.right.preOrderTraverseRecur()

    def preOrderTraverseIter(self):
        s = []
        N_tmp = self

        while True:
            if N_tmp != None:
                N_tmp.printNode()
                if N_tmp.right != None:
                    s.append(N_tmp.right)
                N_tmp = N_tmp.left
            else:
                if len(s) > 0:
                    N_tmp = s.pop()
                else:
                    return

    def inOrderTraverseRecur(self):
        if self.left != None:
            self.left.inOrderTraverseRecur()
        if self != None:
            self.printNode()
        if self.right != None:
            self.right.inOrderTraverseRecur()

    def inOrderTraverseIter(self):
        s = []
        N_tmp = self

        while True:
            if N_tmp != None:
                s.append(N_tmp)
                N_tmp = N_tmp.left
            else:
                if len(s) > 0:
                    N_tmp = s.pop()
                    N_tmp.printNode()
                    N_tmp = N_tmp.right
                else:
                    return

    def postOrderTraverseRecur(self):
        if self.left != None:
            self.left.postOrderTraverseRecur()
        if self.right != None:
            self.right.postOrderTraverseRecur()
        if self != None:
            self.printNode()

    def postOrderTraverseIter(self):
        s = []
        lastVisited = None
        N_tmp = self

        while len(s)>0 or N_tmp != None:
            if N_tmp != None:
                s.append(N_tmp)
                N_tmp = N_tmp.left
            else:
                N_tmp1 = s[-1]
                if N_tmp1.right != None and lastVisited != N_tmp1.right:
                    N_tmp = N_tmp1.right
                else:
                    N_tmp1.printNode()
                    lastVisited = s.pop()

    def printNode(self):
        print self.data,

def findLowestCommonAncestorRecur(root, N1, N2):
    if root == None:
        return
    left = right = None
    if root == N1 or root == N2:
        return root

    if root.left != None:
        left = findLowestCommonAncestorRecur(root.left, N1, N2)
    if root.right != None:
        right = findLowestCommonAncestorRecur(root.right, N1, N2)
    if left and right:
        return root
    else:
        return left or right

def findLowestCommonAncestorIter(root, N1, N2):
    if root == None:
        return
    q = Queue.Queue()
    dt = {}
    q.put(root)

    while not q.empty():
        cur = q.get()
        if cur.left != None:
            q.put(cur.left)
            dt[cur.left] = cur
        if cur.right != None:
            q.put(cur.right)
            dt[cur.right] = cur

    l1 = []
    l2 = []
    tmp = N1
    while tmp != None:
        l1.append(tmp)
        tmp = dt.get(tmp, None)
    tmp = N2
    while tmp != None:
        l2.append(tmp)
        tmp = dt.get(tmp, None)

    last = None
    while len(l1) > 0 and len(l2) > 0:
        t1 = l1.pop()
        t2 = l2.pop()
        if t1 == t2:
            last = t1
        else:
            break
    return last

if __name__ == "__main__":
    # buid a binary tree
    N6 = Node(6)
    N7 = Node(7)
    N4 = Node(4)
    N5 = Node(5)
    N5.addLeft(N6)
    N5.addRight(N7)
    N2 = Node(2)
    N2.addLeft(N4)
    N2.addRight(N5)
    N3 = Node(3)
    N1 = Node(1)
    N1.addLeft(N2)
    N1.addRight(N3)

    # breath-first Traverse
    print "breath-first Traverse: ",
    N1.breathFirstTraverse()
    print ""

    # preOrderTraverse
    print "preOrderTraverseRecur: ",
    N1.preOrderTraverseRecur()
    print ""
    print "preOrderTraverseIter: ",
    N1.preOrderTraverseIter()
    print ""

    # inOrderTraverse
    print "inOrderTraverseRecur: ",
    N1.inOrderTraverseRecur()
    print ""
    print "inOrderTraverseIter: ",
    N1.inOrderTraverseIter()
    print ""

    # postOrderTraverse
    print "postOrderTraverseRecur: ",
    N1.postOrderTraverseRecur()
    print ""
    print "postOrderTraverseIter: ",
    N1.postOrderTraverseIter()
    print ""

    print "lowest common ancestor Recur: ",
    findLowestCommonAncestorRecur(N1, N3, N5).printNode()
    print ""
    print "lowest common ancestor Iter: ",
    findLowestCommonAncestorIter(N1, N3, N5).printNode()
