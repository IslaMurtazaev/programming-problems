from typing import List

# Number of Islands https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1380/


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        island_counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    island_counter += 1
                    stack = [[i, j]]
                    self.markIslandTerritory(grid, island_counter, stack)

        return island_counter

    def markIslandTerritory(self, grid, island_num, island_territory):
        while island_territory:
            y, x = island_territory.pop()
            grid[y][x] = island_num
            self.addNeigbors(y, x, grid, island_territory)

    def addNeigbors(self, y, x, grid, stack):
        neighbors = []
        if y + 1 < len(grid):
            neighbors.append([y+1, x])
        if x + 1 < len(grid[0]):
            neighbors.append([y, x+1])
        if y - 1 >= 0:
            neighbors.append([y-1, x])
        if x - 1 >= 0:
            neighbors.append([y, x-1])
        for n_y, n_x in neighbors:
            if grid[n_y][n_x] == '1':
                stack.append([n_y, n_x])
