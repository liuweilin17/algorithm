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
        # create graph based on similar words
        N = len(wordList)
        M = len(beginWord)
        dt = collections.defaultdict(list)
        for i in range(N):
            word = wordList[i]
            for j in range(M):
                dt[word[:j]+'*'+word[j+1:]].append(word)
        
        # dt creates a graph between different words.
        # bfs to find the shortest path
        visited = [beginWord] # word, level
        Q = Queue()
        Q.put((beginWord, 1))
        while not Q.empty():
            word, level = Q.get()
            for i in range(M):
                inter_word = word[:i] + '*' + word[i+1:]
                for nei in dt[inter_word]:
                    if nei not in visited:
                        if nei == endWord:
                            return level+1
                        Q.put((nei, level+1))
                        visited.append(nei)
                dt[inter_word] = [] # TLE if not without this line
        return 0

    # without the use of visited
    def ladderLength3(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # create graph based on similar words
        N = len(wordList)
        M = len(beginWord)
        dt = collections.defaultdict(list)
        for i in range(N):
            word = wordList[i]
            for j in range(M):
                dt[word[:j]+'*'+word[j+1:]].append(word)

        # dt creates a graph between different words.
        # bfs to find the shortest path
        # visited = [beginWord] # word, level
        Q = Queue()
        Q.put((beginWord, 1))
        while not Q.empty():
            word, level = Q.get()
            for i in range(M):
                inter_word = word[:i] + '*' + word[i+1:]
                for nei in dt[inter_word]:
                    if nei == endWord:
                        return level+1
                    Q.put((nei, level+1))
                dt[inter_word] = [] # TLE if not without this line
        return 0


