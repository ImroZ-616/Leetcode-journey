class Solution:
    def assignEdgeWeights(self, edges):
        mod = 10**9 + 7
        
        n = len(edges) + 1
        
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        from collections import deque
        
        q = deque()
        q.append((1, 0))
        vis = [False] * (n + 1)
        vis[1] = True
        
        max_depth = 0
        
        while q:
            node, d = q.popleft()
            max_depth = max(max_depth, d)
            
            for nei in g[node]:
                if not vis[nei]:
                    vis[nei] = True
                    q.append((nei, d + 1))
        
        if max_depth == 0:
            return 0
        
        return pow(2, max_depth - 1, mod)