###########################################
# Let's Have Some Fun
# File Name: merge_sort.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu May  2 17:25:07 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#MergeSort
#1. worst case: O(nlogn)
#2. best case: O(nlogn)
#3. average case: O(nlogn)
#4. out of place, O(n)
#5. stable because of L[i] <= R[j]

class MergeSort:
    def merge(self, A, p, q, r):
        n1 = q - p + 1
        n2 = r - q
        L = (n1+1) * [0]
        R = (n2+1) * [0]
        for i in range(n1):
            L[i] = A[p + i]
        for j in range(n2):
            R[j] = A[q+1+j]
        L[n1] = float('inf')
        R[n2] = float('inf')
        i, j = 0, 0
        for k in range(p, r+1):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1

    def merge_sort(self, A, p, r):
        if p < r:
            q = (p + r) // 2
            self.merge_sort(A, p, q)
            self.merge_sort(A, q+1, r)
            self.merge(A, p, q, r)

def showMergeSort(A):
    s = MergeSort()
    print(A)
    s.merge_sort(A, 0, len(A)-1)
    print(A)

if __name__ == '__main__':
    print('-------case 1---------')
    A = [2, 3, 1, 4]
    showMergeSort(A)
    print('-------case 2---------')
    A = []
    showMergeSort(A)
    print('-------case 3---------')
    A = [1]
    showMergeSort(A)
    print('-------case 4---------')
    A = [1,2,1]
    showMergeSort(A)


