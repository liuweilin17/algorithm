###########################################
# Let's Have Some Fun
# File Name: 68.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Sep 26 09:47:56 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#68. Text Justification

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = []
        N = len(words)
        arr_tmp = []
        len_tmp = 0
        for i in range(N):
            # print(len_tmp, arr_tmp)
            word = words[i]
            arr_tmp.append(word)
            if len_tmp == 0:
                len_tmp += len(word)
            else:
                len_tmp += len(word) + 1

            if len_tmp == maxWidth:
                ret.append(' '.join(arr_tmp))
                arr_tmp = []
                len_tmp = 0
            elif len_tmp > maxWidth:
                arr_tmp = arr_tmp[:-1]
                if len(arr_tmp) == 1:
                    ret.append(arr_tmp[0] + (maxWidth-len(arr_tmp[0]))*' ')
                else:
                    l = maxWidth - sum([len(w) for w in arr_tmp])
                    k = len(arr_tmp) - 1
                    a, b = l//k, l%k
                    t = ''
                    for j in range(k):
                        if j < b:
                            t += arr_tmp[j] + ' ' * (a + 1)
                        else:
                            t += arr_tmp[j] + ' ' * a
                    t += arr_tmp[-1]
                    ret.append(t)
                arr_tmp = [word]
                len_tmp = len(word)
            else: pass

        if arr_tmp:
            # last line
            t1 = ' '.join(arr_tmp)
            t2 = ' ' * (maxWidth - len(t1))
            ret.append(t1 + t2)

        return ret


