class DSU:
    def __init__(self, n):
        self.Parent = list(range(n+1))
        self.Size = [1] * (n+1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2: return
        if self.Size[p1] >= self.Size[p2]:
            self.Size[p1] += self.Size[p2]
            self.Parent[p2] = p1
        else:
            self.Size[p2] += self.Size[p1]
            self.Parent[p1] = p2

    def getsize(self, node):
        return self.Size[self.find(node)]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dsu = DSU(rows * cols)
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: continue
                for dr, dc in directions:
                    gr, gc = r + dr, c + dc
                    if (gr < 0 or gc < 0 or gr == rows or gc == cols or
                    grid[gr][gc] == 0): continue
                    dsu.union(r*cols+c, gr*cols+gc)
                area = max(area, dsu.getsize(r*cols+c))
        return area