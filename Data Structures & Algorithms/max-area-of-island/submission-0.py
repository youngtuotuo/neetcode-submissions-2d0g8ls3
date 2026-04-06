class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        directions = ((1,0), (-1,0), (0,1), (0,-1))
        def dfs(r,c):
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            res = 1
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    gr, gc = r + dr, c + dc
                    if (gr < 0 or gc < 0 or gr == rows or gc == cols
                        or grid[gr][gc] == 0): continue
                    grid[gr][gc] = 0
                    q.append((gr, gc))
                    res += 1
            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: continue
                res = max(res, dfs(r,c))
        return res
        