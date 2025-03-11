class DSU:
    def __init__(self):
        self.roots = {}
        self.parents = {}
    
    def count(self):
        roots = set()
        for r in self.roots:
            roots.add(self.find(r))
        return len(roots)
    
    def find(self, id):
        while self.roots[id] != id:
            id = self.roots[id]

        return id
    
    def ensure_node(self, n):
        if self.roots.get(n, None) is None:
            self.roots[n] = n

        if self.parents.get(n, None) is None:
            self.parents[n] = set()

    def union(self, a, b):
        self.ensure_node(a)
        self.ensure_node(b)
        
        if a != b:
            self.parents[a].add(b)
            self.parents[b].add(a)
    
        a = self.find(a)
        b = self.find(b)
        if a != b:
            self.roots[b] = a

class Solution:
    def isDisconnected(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        uf = DSU()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                
                id = m*i + j
                uf.union(id, id)

                # Right
                if j < m - 1 and grid[i][j+1] == 1:
                    uf.union(id, id + 1)

                # Down
                if i < n - 1 and grid[i+1][j] == 1:
                    uf.union(id, (m*(i+1) + j))
                
                # Up
                if i > 0 and grid[i-1][j] == 1:
                    uf.union(id, (m*(i-1) + j))

                # Left
                if j > 0 and grid[i][j-1] == 1:
                    uf.union(id, id - 1)
        
        count = uf.count()
        return count == 0 or count > 1

    def minDays(self, grid: List[List[int]]) -> int:
        if self.isDisconnected(grid):
            return 0
        
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if self.isDisconnected(grid):
                        return 1
                    grid[i][j] = 1
                    
        return 2