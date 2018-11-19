###########################################
# Let's Have Some Fun
# File Name: 943.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Nov 18 19:16:37 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 943. Find the Shortest Superstring

'''
function algorithm TSP (G, n)
  for k := 2 to n do
    C({k}, k) := d1,k
  end for

  for s := 2 to n-1 do
    for all S ⊆ {2, . . . , n}, |S| = s do
      for all k ∈ S do
        C(S, k) := minm≠k,m∈S [C(S\{k}, m) + dm,k]
      end for
    end for
  end for

  opt := mink≠1 [C({2, 3, . . . , n}, k) + dk,1]
  return (opt)
end
'''

class Solution:
    # the length of common substr
    def calD(self, s1, s2):
        ans = 0
        l1 = len(s1)
        l2 = len(s2)
        for i in range(l1):
            if s2.startswith(s1[i:]):
                ans = l1 - i
                break
        return ans

    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        N = len(A)
        graph = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if i != j:
                    graph[i][j] = self.calD(A[i], A[j])

        # dp[mask][i] is the min length of mask subset ending with i
        dp = [[0] * N for _ in range(1 << N)]
        # parent[mask][i] is the parent of i, which is the ending of i in mask subset with min length
        parent = [[None] * N for _ in range(1 << N)]
        for mask in range(1, 1 << N):
            for bit in range(N):
                # bit is in mask
                if (mask >> bit) & 1:
                    # remove bit from mask
                    pmask = (1 << bit) ^ mask
                    if pmask == 0: continue
                    for k in range(N):
                        if (pmask >> k) & 1:
                            value = dp[pmask][k] + graph[k][bit]
                            if value > dp[mask][bit]:
                                dp[mask][bit] = value
                                parent[mask][bit] = k

        # find parents
        perm = []
        mask = (1 << N) - 1
        maxInd = dp[mask].index(max(dp[mask]))
        i = maxInd
        while i is not None:
            bak = i
            perm.append(i)
            i = parent[mask][i]
            mask = mask ^ (1 << bak)
            #mask, i = mask ^ (1 << i), parent[mask][i]

        # reverse
        perm = perm[::-1]
        seen = [False] * N
        for i in perm:
            seen[i] = True
        perm.extend([i for i in range(N) if not seen[i]])
        print(perm)


        # construct result
        ret = A[perm[0]]
        for i in range(1, N):
            j = perm[i]
            k = perm[i-1]
            pref = graph[k][j]
            ret += A[j][pref:]
        return ret

if __name__ == '__main__':
    s = Solution()
    #print(s.shortestSuperstring(["alex","loves","leetcode"]))
    print(s.shortestSuperstring(["sssv","svq","dskss","sksss"]))

