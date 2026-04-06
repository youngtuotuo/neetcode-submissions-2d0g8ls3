class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        res = 0

        def bfs(r, c):
            if (r < 0 or c < 0 or r == rows or c == cols
                or grid[r][c] == 0): return 0

            q = deque()
            q.append((r, c))
            size = 1
            grid[r][c] = 0
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    gr, gc = r + dr, c + dc
                    if (gr < 0 or gc < 0 or gr == rows or gc == cols or
                        grid[gr][gc] == 0): continue
                    q.append((gr, gc))
                    grid[gr][gc] = 0
                    size += 1
            return size


        for r in range(rows):
            for c in range(cols):
                res = max(res, bfs(r, c))

        return res
