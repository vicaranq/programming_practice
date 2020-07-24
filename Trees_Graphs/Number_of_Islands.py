'''
https://leetcode.com/problems/number-of-islands/

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and
is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

'''

import queue


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        def getAdjs(coordinate):
            result = []
            row, col = coordinate
            # top
            if row - 1 >= 0:
                result.append((row-1,col))
            # bottom
            if row + 1 < len(grid):
                result.append((row + 1, col))
            # right
            if col + 1 < len(grid[0]):
                result.append((row,col+1))
            # left
            if col - 1 >= 0:
                result.append((row, col-1))
            return result # list of tuples


        pq = queue.PriorityQueue()
        visited = set()
        visiting = set()

        numIslands = 0
        inIsland = False

        row, col = (0,0)
        val = int(grid[row][col])

        n = (val*(-1), (row, col)) # multiplying by -1 to make 1 a priority over 0

        pq.put(n)

        while not pq.empty():

            n = pq.get()

            row, col = n[1]
            val = int(grid[row][col])

            visited.add((row, col))

            if not inIsland and val == 1:
                numIslands += 1

            inIsland = (val == 1)

            # find adjacent coords
            adjs = getAdjs((row,col))

            for adj in adjs:

                if adj not in visited and adj not in visiting:

                    x, y = adj
                    adj_val = int(grid[x][y])

                    n = (adj_val*(-1),(x,y))
                    pq.put(n)
                    visiting.add((x,y))

                    if adj_val == 1 and val == 0:
                        break

        return numIslands
