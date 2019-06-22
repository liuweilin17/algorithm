###########################################
# Let's Have Some Fun
# File Name: 5087.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun  9 Jun 12:49:20 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#1079. Letter Tile Possibilities

class Solution:
    # https://leetcode.com/problems/letter-tile-possibilities/discuss/308284/Concise-java-solution
    def numTilePossibilities(self, tiles: str) -> int:
        arr = [0] * 26
        for c in tiles:
            arr[ord(c) - ord('A')] += 1

        def dfs(arr):
            count = 0
            for i in range(26):
                if arr[i] == 0: continue
                # add char i to the current string
                count += 1
                arr[i] -= 1
                count += dfs(arr)
                arr[i] += 1
            return count

        return dfs(arr)

