# 589. N-ary Tree Preorder Traversal

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    # This is based on first version of preOrder Traverse
    def preorder1(self, root):
        """
        :type root: Node
        :rtype List[int]
        """
        if not root:
            return []
        ret = []
        st = []
        st.append(root)
        while len(st):
            nd = st.pop()
            while nd:
                ret.append(nd.val) # get the node
                for i in range(len(nd.children)-1): # reverse order
                    st.append(nd.children[-i-1])
                if nd.children:
                    nd = nd.children[0]
                else:
                    nd = None
        return ret

    # This is based on second version of preOrder Distance
    def preorder2(self, root):
        if not root:
            return []
        ret = []
        st = []
        st.append(root)
        while len(st):
            nd = st.pop()
            ret.append(nd.val)
            if nd.children:
                for i in range(len(nd.children)):
                    st.append(nd.children[-i-1])
        return ret
