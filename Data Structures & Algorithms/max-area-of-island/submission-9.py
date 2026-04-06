class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        amount = rows * cols
        parents = list(range(amount + 1))
        sizes = [1] * (amount + 1)
        area = 0
        directions = ((1,0), (-1,0), (0,1), (0,-1))

        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2: return
            if sizes[p1] >= sizes[p2]:
                sizes[p1] += sizes[p2]
                parents[p2] = p1
            else:
                sizes[p2] += sizes[p1]
                parents[p1] = p2

        def size(node):
            return sizes[parents[node]]

        def index(r, c):
            return r * cols + c

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: continue
                for dr, dc in directions:
                    gr, gc = r + dr, c + dc
                    if (gr < 0 or gc < 0 or gr >= rows or gc >= cols or
                        grid[gr][gc] == 0):
                        continue
                    union(index(r, c), index(gr, gc))
                area = max(area, size(index(r, c)))
        return area