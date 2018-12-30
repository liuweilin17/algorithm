import queue

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, x): # x is an array of elements
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

# traverse with BFS
# use Queue
# put root first
# each line represents a layer in tree(by count !!!)
def printTreeBFS(root):
    if root == None:
        return None
    q = queue.Queue()
    q.put(root)
    count = 1
    depth = 0
    while not q.empty():
        nd = q.get()
        if nd != None:
            print(str(nd.val) + ', ', end='')
        else:
            print('null, ', end='')
        count -= 1
        if nd:
            q.put(nd.left)
            q.put(nd.right)
        if count == 0:
            count = q.qsize()
            print('')
            depth += 1

def printTreePreOrder(root):
    pass

def printTreeInOrder(root):
    if root == None: return None
    stk = []
    nd = root
    while nd or len(stk):
        while nd:
            stk.append(nd)
            nd = nd.left
        nd = stk.pop()
        print(nd.val, end=',')
        nd = nd.right

def printTreePostOrder(root):
    pass





