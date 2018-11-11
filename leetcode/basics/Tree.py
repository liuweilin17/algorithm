class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, x): # x is a list
        self.root = self.makeTree(0,x)

    def makeTree(self, ind, x):
        if ind >= len(x) or x[ind] == 'null':
            return None
        else:
            n = TreeNode(x[ind])
            n.left = self.makeTree(2*ind + 1, x)
            n.right = self.makeTree(2*ind + 2, x)
            return n

    def getRoot(self):
        return self.root


