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
    if not root:
        return
    q = queue.Queue()
    q.put(root)
    count = 1
    depth = 0
    while not q.empty():
        nd = q.get()
        if nd != None:
            print(str(nd.val) + ', ', end='')
        else:
            #print('null, ', end='')
            pass
        count -= 1
        if nd:
            q.put(nd.left)
            q.put(nd.right)
        if count == 0:
            count = q.qsize()
            print('')
            depth += 1

def printTreePreOrderRec(root):
    if root:
        print(root.val, end=',')
        if root.left:
            printTreePreOrderRec(root.left)
        if root.right:
            printTreePreOrderRec(root.right)

def printTreeInOrderRec(root):
    if root:
        if root.left:
            printTreeInOrderRec(root.left)
        print(root.val, end=',')
        if root.right:
            printTreeInOrderRec(root.right)

def printTreePostOrderRec(root):
    if root:
        if root.left:
            printTreePostOrderRec(root.left)
        if root.right:
            printTreePostOrderRec(root.right)
        print(root.val, end=',')

# Try not to memorize the code but understand
def printTreePreOrder(root):
    if not root:
        return
    st = []
    st.append(root)
    while len(st):
        nd = st.pop()
        while nd:
            print(nd.val, end=',')
            if nd.right:
                st.append(nd.right)
            nd = nd.left
    print('')

# This a version easy to understand
# And is quite similar to BFS
# And is easier to be used for DFS
def printTreePreOrder1(root):
    if not root:
        return
    st = []
    st.append(root)
    while len(st):
        nd = st.pop()
        print(nd.val, end=',')
        if nd.right:
            st.append(nd.right)
        if nd.left:
            st.append(nd.left)
    print('')

# This is final version
def printTreeInOrder(root):
    if not root: return None
    stk = []
    nd = root
    while nd or len(stk):
        while nd:
            stk.append(nd)
            nd = nd.left
        nd = stk.pop()
        print(nd.val, end=',')
        nd = nd.right
    print('')

# This is similar to printTreeInOrder, which easier to understand
def printTreeInOrder1(root):
    if not root: return
    st = []
    nd = root
    while len(st) or nd:
        while nd:
            st.append(nd)
            nd = nd.left
        nd = st.pop()
        print(nd.val, end=',')
        if nd.right:
            nd = nd.right
        else:
            nd = None
    print('')

def printTreePostOrder(root):
    pass





