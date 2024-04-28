class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        out = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    if i == row - 1:
                        out += 1
                    if i == 0:
                        out += 1

                    if j == col - 1:
                        out += 1
                    if j == 0:
                        out += 1
                    try:
                        if grid[i][j + 1] == 0:
                            out += 1
                    except:
                        pass

                    jj = j - 1
                    if jj > -1:
                        if grid[i][jj] == 0:
                            out += 1
                    try:
                        if grid[i + 1][j] == 0:
                            out += 1
                    except:
                        pass

                    ii = i - 1
                    if ii > -1:
                        if grid[i - 1][j] == 0:
                            out += 1

        return out

