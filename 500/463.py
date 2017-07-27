class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += self.get_perimter_sum(i, j, grid)
        return res

    def get_perimter_sum(self, i, j, grid):
        neighbour = [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]
        count = 0
        for x, y in neighbour:
            if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] != 1:
                count += 1
        return count

if __name__ == "__main__":
    s = Solution()
    grids = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    result = s.islandPerimeter(grids)
    print(result)