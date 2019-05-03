###########################################
# Let's Have Some Fun
# File Name: bubble_sort.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu May  2 17:25:43 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#BubbleSort
#1. worst case: O(n^2)
#2. best case: O(n^2)
#3. average case: O(n^2)
#4. in place
#5. stable

class BubbleSort:
    def bubble_sort(self, A):
        N = len(A)
        for i in range(N-1):
            for j in range(N-1, i, -1):
                if A[j] < A[j-1]:
                    tmp = A[j]
                    A[j] = A[j-1]
                    A[j-1] = tmp

def showBubbleSort(A):
    s = BubbleSort()
    print(A)
    s.bubble_sort(A)
    print(A)

if __name__ == '__main__':
    print('-------case 1---------')
    A = [2, 3, 1, 4]
    showBubbleSort(A)
    print('-------case 2---------')
    A = []
    showBubbleSort(A)
    print('-------case 3---------')
    A = [1]
    showBubbleSort(A)
    print('-------case 4---------')
    A = [1,2,1]
    showBubbleSort(A)

