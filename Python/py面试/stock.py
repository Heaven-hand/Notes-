class Solution:
    def minPathSum(grid) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(1,m):
            grid[i][0] += grid[i-1][0]
        for i in range(1,n):
            grid[0][i] += grid[0][i-1]
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j == 0:
        #             continue
        #         grid[i][j] = grid[i][j] + min(grid[i-1][j],grid[i][j-1])
        print(grid)
        return grid[m-1][n-1]
Solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]])