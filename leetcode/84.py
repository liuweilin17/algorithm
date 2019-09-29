###########################################
# Let's Have Some Fun
# File Name: 84.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Sep 27 11:00:23 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 84. Largest Rectangle in Histogram

class SegmentNode:
    def __init__(self, begin, end):
        self.min_v = -1
        self.begin = begin
        self.end = end
        self.left = None
        self.right = None

class Solution:
	# O(n^3), time limit exceed
    def largestRectangleArea1(self, heights: List[int]) -> int:
        N = len(heights)
        ret = 0
        for i in range(N):
            for j in range(i, N):
                ret = max(ret, min(heights[i:j+1])*(j-i+1))
        
        return ret

    # O(n^2), time limit exceed
    def largestRectangleArea2(self, heights: List[int]) -> int:
        N = len(heights)
        ret = 0
        for i in range(N):
            min_h = heights[i]
            for j in range(i, N):
                min_h = min(min_h, heights[j])
                ret = max(ret, min_h*(j-i+1))
        
        return ret

    # divide and conquer
    # the maximum area of rectangle is one of these:
    # 1. minimum height * number of bars
    # 2. maximum area of bars on the left of minimum height
    # 3. maximum area of bars on the right of minimum height
    # average O(nlogn)
    # worst O(n^2) when heights are sorted
    # time limit exceed
    def largestRectangleArea3(self, heights: List[int]) -> int:
        def helper(begin, end):
            if begin > end: return 0
            min_ind = begin
            min_height = heights[min_ind]
            for i in range(begin+1, end+1):
                if heights[i] < min_height:
                    min_ind = i
                    min_height = heights[i]
            a1 = min_height * (end - begin + 1)
            a2 = helper(begin, min_ind-1)
            a3 = helper(min_ind+1, end)
            return max([a1, a2, a3])
        
        N = len(heights)
        return helper(0, N-1)

    # divide and conquer with segment tree
    def largestRectangleArea4(self, heights: List[int]) -> int:
        # build segment tree for find mininum value in heights
        def buildSegmentTree(begin, end):
            if begin > end: return None
            root = SegmentNode(begin, end)
            if begin == end:
                root.min_v = begin
                return root
            else:        
                middle = (begin + end) // 2
                root.left = buildSegmentTree(begin, middle)
                root.right = buildSegmentTree(middle+1, end)
                root.min_v = root.left.min_v if heights[root.left.min_v] < heights[root.right.min_v] else root.right.min_v
                return root
        
        # find the mininum value in segment tree
        def query(nd, begin, end):
            if nd == None or begin > nd.end or end < nd.begin:
                return -1
            # I don't know why, check the review updates below this solution
            if begin <= nd.begin and end >= nd.end:
                return nd.min_v
            left_min = query(nd.left, begin, end)
            right_min = query(nd.right, begin, end)
            if left_min == -1: return right_min
            if right_min == -1: return left_min
            return left_min if heights[left_min] < heights[right_min] else right_min
        
        def helper(begin, end):
            if begin > end: return 0
            elif begin == end: return heights[begin]
            else: pass
            min_ind = query(root, begin, end)
            print(begin, end, min_ind)
            min_height = heights[min_ind]
            a1 = min_height * (end - begin + 1)
            a2 = helper(begin, min_ind-1)
            a3 = helper(min_ind+1, end)
            return max([a1, a2, a3])
        
        N = len(heights)
        root = buildSegmentTree(0, N-1)
        return helper(0, N-1)
    
    # stack
    # st[-1] is the local maximum heights, we calcuate the area from its left to st[-1], all the heights on the left is in the stack and smaller than it
    def largestRectangleArea5(self, heights: List[int]) -> int:
        st = [-1] # use -1 to calculate the minimum width
        N = len(heights)
        max_area = 0
        for i in range(N):
            while st[-1] != -1 and heights[st[-1]] >= heights[i]:
                max_area = max(max_area, heights[st.pop()] * (i - st[-1] - 1))
            st.append(i)
        while st[-1] != -1:
            max_area = max(max_area, heights[st.pop()] * (len(heights) - st[-1] -1))
        return max_area
      
        