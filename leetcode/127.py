###########################################
# Let's Have Some Fun
# File Name: 127.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed May  1 21:38:53 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#127. Word Ladder

class Solution:
    # dijkstra, time limit exceed
    def ladderLength1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        wordList.append(beginWord)

        def onediff(s1, s2):
            count = 0
            N = len(s1)
            for i in range(N):
                if s1[i] != s2[i]:
                    count += 1
            return count == 1

        N = len(wordList)
        # create adjacent list
        adj_list = collections.defaultdict(list)
        for i in range(N):
            for j in range(N):
                if onediff(wordList[i], wordList[j]):
                    adj_list[i].append(j)

        # djkstra
        Q, dist = [], []
        for i in range(N):
            Q.append([N+2, i])
            dist.append(N+2)
        Q[N-1] = [0, N-1]
        dist[N-1] = 0
        heapq.heapify(Q)
        while Q:
            # print(Q)
            minNd = heapq.heappop(Q)[1]
            for nei in adj_list[minNd]:
                if dist[nei] > dist[minNd] + 1:
                    dist[nei] = dist[minNd] + 1
                    for i in range(len(Q)):
                        if Q[i][1] == nei:
                            Q[i][0] = dist[nei]
                    heapq.heapify(Q)
        # print(dist)
        for i in range(N):
            if wordList[i] == endWord:
                return dist[i] + 1 if dist[i] != N+2 else 0

    # BFS.
    # N: length of words, M: number of words
    # time comlexity: O(MN)
    # space comlexity: O(MN)
    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        
        N = len(beginWord)
        # create dict, intermediate_word -> original word
        # to reduce the time complexity of finding one character different of string
        dt = collections.defaultdict(list)
        for word in wordList:
            for i in range(N):
                dt[word[:i] + '*' + word[i+1:]].append(word)
                
        # BFS
        Q = Queue()
        Q.put((beginWord, 1))
        visited = [beginWord]
        while not Q.empty(): # Notice while not Q will be wrong !!!
            word, level = Q.get()
            for i in range(N):
                intermediate_word = word[:i] + '*' + word[i+1:]
                for wordd in dt[intermediate_word]:
                    if wordd == endWord:
                        return level + 1
                    if wordd not in visited:
                        Q.put((wordd, level+1))
                        visited.append(wordd)
                dt[intermediate_word] = []
                
        return 0



