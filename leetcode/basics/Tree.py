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
def breadthFirstTraversal(root):
    if not root:
        return
    ret = []
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        count = q.qsize()
        seq = []
        for i in range(count):
            nd = q.get()
            seq.append(nd.val)
            if nd.left: q.put(nd.left)
            if nd.right: q.put(nd.right)
        ret.append(seq[:])
    return ret

# preorder DFS
# recursive version, easy
def preOrderTraversalRec(root):
    def dfs(nd, ret):
        if nd:
            ret.append(nd.val)
            if nd.left: dfs(nd.left, ret)
            if nd.right: dfs(nd.right, ret)
    ret = []
    dfs(root, ret)
    return ret

# preorder DFS
# use Stack
# iterative version1, easy to understand
def preOrderTraversalIter1(root):
    if not root: return []
    ret = []
    st = []
    st.append(root)
    while len(st):
        nd = st.pop()
        ret.append(nd.val)
        if nd.right: st.append(nd.right)
        if nd.left: st.append(nd.left)
    return ret

# preorder DFS
# use Stack
# iterative version2, visit all the left and add the right node to the stack
def preOrderTraversalIter2(root):
    if not root: return []
    ret = []
    st = [root]
    while len(st):
        nd = st.pop()
        while nd:
            ret.append(nd.val)
            if nd.right: st.append(nd.right)
            nd = nd.left
    return ret

# inorder DFS
# recursive version, easy
def inOrderTraversalRec(root):
    def dfs(nd, ret):
        if nd:
            if nd.left: dfs(nd.left, ret)
            ret.append(nd.val)
            if nd.right: dfs(nd.right, ret)
    ret = []
    dfs(root, ret)
    return ret

# inorder DFS
# iterative version
# use Stack
# keep visit the left child and then the right child
def inOrderTraversalIter(root):
    if not root: return []
    ret = []
    st = []
    nd = root
    while len(st) or nd:
        while nd:
            st.append(nd)
            nd = nd.left
        nd = st.pop()
        ret.append(nd.val)
        nd = nd.right
    return ret

# postorder DFS
# recursive method, easy
def postOrderTraversalRec(root):
    def dfs(nd, ret):
        if nd:
            if nd.left: dfs(nd.left, ret)
            if nd.right: dfs(nd.right, ret)
            ret.append(nd.val)
    ret = []
    dfs(root, ret)
    return ret

# postorder DFS
# use Stack
# iterative version1, harder to understand
def postOrderTraversalIter1(root):
    if not root: return []
    ret = []
    st = []
    nd = root
    pre = None
    while len(st) or nd:
        while nd: # put left child in the stack
            st.append(nd)
            nd = nd.left
        nd = st[-1]
        if pre and nd.right == pre: # the right child of nd is visited
            ret.append(nd.val)
            st.pop()
            pre = nd
            nd = None # next nd obtained from the stack
        else:
            if not nd.right: # no right child
                ret.append(nd.val)
                st.pop()
                pre = nd
            nd = nd.right
    return ret

# postorder DFS
# use Stack
# iterative version 2, reverse the result of preorder(root->right->left)
def postorderTraversalIter2(root):
    if not root: return []
    ret = []
    st = []
    st.append(root)
    while len(st):
        nd = st.pop()
        ret.append(nd.val)
        if nd.left: st.append(nd.left)
        if nd.right: st.append(nd.right)
    return ret[::-1] # reverse

# !!! reverse the result of preorder(root->right->left) !!!!
def printTreePostOrder2(root):
    if not root: return
    st = []
    ret = []
    st.append(root)
    while len(st):
        nd = st.pop()
        print(nd.val, ',')
        if nd.left: st.append(nd.left)
        if nd.right: st.append(nd.right)

if __name__ == '__main__':
    t = BinaryTree([1, 2, 3, 'null', 'null', 4, 5])
    print(breadthFirstTraversal(t.root))
    print(preOrderTraversalRec(t.root))
    print(preOrderTraversalIter1(t.root))
    print(preOrderTraversalIter2(t.root))
    print(inOrderTraversalRec(t.root))
    print(inOrderTraversalIter(t.root))
    print(postOrderTraversalRec(t.root))
    print(postOrderTraversalIter1(t.root))
    print(postorderTraversalIter2(t.root))



