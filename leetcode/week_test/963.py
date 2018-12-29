###########################################
# Let's Have Some Fun
# File Name: 963.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Dec 29 12:10:38 2018
###########################################
#coding=utf-8
#!/usr/bin/python
import itertools
import collections

class Solution:
    # this is first method given in the solution
    # find all permutations of three points, then calculate the fourth point
    # if the fourth point exists, calculate the area
    # details could be found in Solution of Leetcode
    # time: O(N^3)
    # space: O(N)
    def minAreaFreeRect1(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        EPS = 1e-5
        points = set(map(tuple, points))
        ret = float('inf')
        for p1, p2, p3 in itertools.permutations(points, 3):
            p4 = (p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1])
            if p4 in points:
                v31 = complex(p3[0]-p1[0], p3[1]-p1[1])
                v21 = complex(p2[0]-p1[0], p2[1]-p1[1])
                # notice, there is abs on the dot product
                if abs(v31.real * v21.real + v31.imag * v21.imag) < EPS:
                    area = abs(v31) * abs(v21)
                    if area < ret:
                        ret = area
        return ret if ret < float('inf') else 0

    # all pairs of two points who share same center and radius are four points of rectangle
    def minAreaFreeRect2(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        ret = float('inf')
        points = [complex(*z) for z in points] # *z unpack each point
        seen = collections.defaultdict(list) # seen: dict, default value is []
        for P,Q in itertools.combinations(points, 2):
            center = (P + Q) / 2.0
            radius = abs(P - center)
            seen[center, radius].append(P)
        for (center, radius), candidates in seen.items():
            for P, Q in itertools.combinations(candidates, 2):
                Q_ = 2 * center - Q
                area = abs(P-Q) * abs(P-Q_)
                if area < ret:
                    ret = area

        return ret if ret < float('inf') else 0




if __name__ == '__main__':
    s = Solution()
    print(s.minAreaFreeRect1([[1,2],[2,1],[1,0],[0,1]]))
    print(s.minAreaFreeRect1([[0,3],[1,2],[3,1],[1,3],[2,1]]))
    print(s.minAreaFreeRect2([[1, 2], [2, 1], [1, 0], [0, 1]]))
    print(s.minAreaFreeRect2([[0, 3], [1, 2], [3, 1], [1, 3], [2, 1]]))




