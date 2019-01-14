# 257. Binary Tree Paths
# Find the path from root to leaves is a basic question

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Recursive
    def binaryTreePaths1(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def binaryTreePathsSub(nd, path, paths):
            if not nd.left and not nd.right:
                paths.append(path)
                return
            path += '->' + str(nd.val) if path != '' else str(nd.val)
            if nd.left:
                binaryTreePathsSub(nd.left, path)
            if nd.right:
                binaryTreePathsSub(nd.right, path)

        if not root:
            return []
        paths = []
        binaryTreePathsSub(root, '', paths)
        return paths

    # Iterative way, this is preorder traverse
    # simply use a stack in the stardard tree traverse is impossible
    # we could use a stack for each node, which memorizes the path from root to this node.
    def binaryTreePaths2(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ret = []
        if not root:
            return ret
        st = []
        st.append((root, str(root.val)))
        while len(st):
            nd, path = st.pop()
            if not nd.left and not nd.right:
                ret.append(path)
                continue
            if nd.left:
                st.append((nd.left, path+'->' + str(nd.left.val)))
            if nd.right:
                st.append((nd.right, path+'->'+str(nd.right.val)))
        return ret


if __name__ == '__main__':
    s = Solution()

