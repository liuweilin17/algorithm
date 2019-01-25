###########################################
# Let's Have Some Fun
# File Name: 722.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Jan 24 20:14:53 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 722. Remove Comments

class Solution:
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        flag = 0 # 0: no comment, 1: line comment, 2: block comment
        ret = []
        pre = None
        tmp = ''
        for s in source:
            for c in s:
                if flag:
                    if flag == 2 and pre == '*' and c == '/':
                        c = None # pre will be None in line45, in case of '*//' or '*/*'
                        flag = 0
                elif pre == '/' and c == '*':
                    tmp = tmp[:-1] # delete previous '/'
                    flag = 2
                    c = None # pre will be None in line45, in case of '/*/'
                elif pre == '/' and c == '/':
                    tmp = tmp[:-1] # delete previous '/'
                    flag = 1
                else:
                    tmp += c
                pre = c
            if flag != 2: # if flag == 2, tmp remain the same for next round
                if flag == 1:
                    flag = 0
                if tmp:
                    ret.append(tmp)
                tmp = ''
            pre = None
        return ret

