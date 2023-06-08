class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        le = len(grid[0])
        for row in grid:
            l , r = 0, le-1
            while l <= r:
                m = (r+l)//2
                if row[m] <0:
                    r = m-1
                else:
                    l = m+1
            c+= (le - l)
        return c
