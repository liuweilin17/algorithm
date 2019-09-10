###########################################
# Let's Have Some Fun
# File Name: 331.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Sep  6 10:53:30 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#331. Verify Preorder Serialization of a Binary Tree

class Solution:
    # time limit exceed, using the method similar to build tree
    def isValidSerialization1(self, preorder: str) -> bool:
        dp = {}
        def helper(preorder):
            if preorder in dp: return dp[preorder]
            N = len(preorder)
            if N == 1:
                dp[preorder] = (preorder[0] == '#')
                return dp[preorder]
            elif preorder[0] == '#':
                dp[preorder] = False
                return dp[preorder]
            else:
                flag = False
                for i in range(2, N):
                    if helper(preorder[1:i]) and helper(preorder[i:]):
                        flag = True
                        break
                dp[preorder] = flag
                return flag

        preorder = preorder.split(",")
        preorder = ['0' if nd != '#' else '#' for nd in preorder]
        # print(preorder)
        return helper(tuple(preorder))
    
    # stack, remove the node when #, # is encountered
    def isValidSerialization2(self, preorder: str) -> bool:
        st = []
        preorder = preorder.split(',')
        for nd in preorder:
            st.append(nd)
            # Notice while is necessary here
            while len(st) > 2 and st[-1] == '#' and st[-2] == '#':
                if st[-3] == '#': return False
                else:
                    st.pop()
                    st.pop()
                    st.pop()
                    st.append('#')
            
        return len(st) == 1 and st[0] == '#'
    
    # indegree <= outdegree at any time, sum of indegree == sum of outdegree 
    def isValidSerialization3(self, preorder: str) -> bool:
        # sum of indegree == sum of outdegree
        # indegree should not be greater than outdegree in the subtree
        degree = -1 # root has 0 indegree, but we add one to degree in the following loop, so we initiate it with -1
        preorder = preorder.split(',')
        for nd in preorder:
            degree += 1
            # Notice degree is checked here
            # for nd may not have child in the sequence
            if degree > 0: return False
            if nd != '#':
                degree -= 2

        return degree == 0




        
