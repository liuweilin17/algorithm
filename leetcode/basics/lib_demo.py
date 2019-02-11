import sys
import collections
import itertools
import heapq
import random
import string

'''
regular python3 lib
'''

# SORT
def testSort():
    # sort the index based on the value
    A = [7,2,5,4]
    B = [2,1,4,3]
    D = {'a':3,'b':2,'c':1}
    print(sorted(range(len(A)), key=A.__getitem__))
    # sort A based on B
    print([ x for x,y in sorted(zip(A,B), key=lambda x:x[1])])
    # sort key based on value in dict
    print(sorted(D.keys(), key=D.get))
    # sort array based on two values
    C = [(2,1),(1,3),(1,-1),(2,-3)]
    print(sorted(C, key=lambda x:(x[0],x[1]))) # sort by v1 and v2(v1 prioritize over v2, both ascending)
    print(sorted(C, key=lambda x:(-x[0],x[1]))) # sort by v1 and v2(v1 prioritize over v2, but v1 descending)

# DATA STRUCTURE
def testArray():
    a = [1,2,3]
    b = [1,2,3]
    print(reversed(a))
    print(a[::-1])
    b.reverse()
    print(b)

def testSet():
    # set is HashSet
    pass

def testMap():
    # dict is HashMap
    pass

def testHeap():
    A = [7, 2, 5, 4]
    heapq.heapify(A) # build heap
    print(A)
    heapq.heappop(A) # pop root
    print(A)
    heapq.heappush(1) # push
    dt = collections.Counter(A)
    print(heapq.nlargest(2, dt.keys(), key=dt.get))
    print(heapq.nsmallest(2, dt.keys(), key=dt.get))

# STRING
def testLower():
    c = 'A'
    print(c.lower())
    print(c.islower())

def testString():
    # in python3
    print(string.ascii_letters)
    print(string.ascii_lowercase)
    print(string.ascii_uppercase)

# MATH
def testInf():
    minV = float('-inf')
    maxV = float('inf')
    maxInt = sys.maxsize
    print('{0},{1},{2}'.format(minV, maxV, maxInt))

def testCollections():
    C = [1, 1, 2, 2, 2, 3, 3]
    count = collections.Counter(C)
    print(count)

def testRandom():
    print(random.randint(2,3)) # random values from [2,3]

def testItertools():
    # itertools.combinations()
    A = [[1,2],[1,3],[1,4]]
    for i,j in itertools.permutations(A, 2):
        print(i, end=',')
        print(j)

def testComplex():
    # complex(real, imag), {real}: real part, {imag}: imaginary part
    a1 = complex(1,1)
    print("real:%s, imaginary:%s" % (a1.real, a1.imag))
    print("abs:%s" %(abs(a1)))

def testScientific():
    # scientific notation
    print(1e-7)

def testBit():
    # BIT
    print(ord('a'))

# OTHER
def testMap1():
    # map(func, list), run func(ele) for ele in list
    points = [[1,2],[2,1],[1,0],[0,1]]
    points = set(map(tuple, points))
    print(points)

if __name__ == '__main__':
    #test
    testString()
