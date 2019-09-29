###########################################
# Let's Have Some Fun
# File Name: 76.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Sep 26 11:42:33 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#76. Minimum Window Substring

class Solution:
    # my solution, faster than 5%, wuwuwu~
    def minWindow1(self, s: str, t: str) -> str:
        dt_t = collections.Counter(t)
        left, right = 0, 0
        N = len(s)
        dt_tmp = collections.Counter("")
        minL = N+1
        ret = ""
        while left <= right and right < N:
            if not dt_t[s[left]]:
                left += 1
                if right < left:
                    right = left
                continue
            if dt_t[s[right]]:
                dt_tmp[s[right]] += 1
            # print(left, right)
            flag = True
            for key in dt_t:
                if dt_tmp[key] < dt_t[key]:
                    flag = False
            if flag:
                # print('equal')
                if right - left + 1 < minL:
                    minL = right - left + 1
                    ret = s[left:right+1]
                dt_tmp[s[left]] -= 1
                left += 1
                dt_tmp[s[right]] -= 1 # dt_tmp[s[right]] will be added by 1
            else:
                right += 1
        return ret

    # optimization of my method
    def minWindow2(self, s: str, t: str) -> str:
        N = len(s)
        minL, begin, end = N+1, 0, -1
        left, right = 0, 0
        matched = 0
        dt_t = collections.Counter(t)
        dt_tmp = {}
        l = len(dt_t)
        while right < N:
            # print(left, right)
            dt_tmp[s[right]] = dt_tmp.get(s[right], 0) + 1
            if dt_tmp[s[right]] == dt_t[s[right]]:
                matched += 1
            while left <= right and matched == l:
                if right - left + 1 < minL:
                    minL, begin, end = right - left + 1, left, right
                dt_tmp[s[left]] -= 1
                if s[left] in dt_t and dt_tmp[s[left]] < dt_t[s[left]]:
                    matched -= 1
                left += 1
            right += 1
        return s[begin:end+1]
    
    # left and right window, with optimized s
    def minWindow3(self, s: str, t: str) -> str:
        dt_t = collections.Counter(t)
        filtered_s = []
        for i, c in enumerate(s):
            if c in dt_t:
                filtered_s.append((i, c))

        N = len(filtered_s)
        minL, begin, end = len(s)+1, 0, -1
        left, right = 0, 0
        matched = 0
        dt_tmp = {}
        l = len(dt_t)

        while right < N:
            # print(left, right)
            c = filtered_s[right][1]
            dt_tmp[c] = dt_tmp.get(c, 0) + 1
            if dt_tmp[c] == dt_t[c]:
                matched += 1
            while left <= right and matched == l:
                dst = filtered_s[right][0] - filtered_s[left][0] + 1
                if dst < minL:
                    minL, begin, end = dst, filtered_s[left][0], filtered_s[right][0]
                dt_tmp[filtered_s[left][1]] -= 1
                if dt_tmp[filtered_s[left][1]] < dt_t[filtered_s[left][1]]:
                    matched -= 1
                left += 1
            right += 1
        return s[begin:end+1]


