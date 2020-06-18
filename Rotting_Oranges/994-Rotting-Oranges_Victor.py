def getRotten(grid):
    assert grid[0]
    rotten_oranges = []
    fresh_oranges_set = set()
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 2:
                rotten_oranges.append((x,y))
            elif grid[x][y] == 1:
                fresh_oranges_set.add((x,y))

    return rotten_oranges, fresh_oranges_set

def getAdjFreshOranges(grid, rotten):

    x, y = rotten
    h = len(grid)
    w = len(grid[0])

    adj_fresh_oranges = []

    # check top
    if x - 1 >= 0 and grid[x-1][y] == 1:
        adj_fresh_oranges.append((x-1, y))

    # check bottom
    if x+1 < h and grid[x+1][y] == 1:
        adj_fresh_oranges.append((x+1,y))

    # check right
    if y+1 < w and grid[x][y+1] == 1:
        adj_fresh_oranges.append((x,y+1))

    # check left
    if y-1 >= 0 and grid[x][y-1] == 1:
        adj_fresh_oranges.append((x,y-1))

    return adj_fresh_oranges

class Solution:

    def orangesRotting(self, grid) -> int:

        if not grid: return -1
        if not grid[0]: return 0

        minutes = 0
        # get coordinates of rotten oranges
        rotten_oranges_to_check, fresh_oranges_set = getRotten(grid) # returns list of (x,y) coordinate for rotten orange

        # if there are not rotten oranges, then return -1
        if not rotten_oranges_to_check and fresh_oranges_set: return  -1
        elif not fresh_oranges_set: return 0

        while rotten_oranges_to_check:
            next_rotten_oranges = []

            for rotten in rotten_oranges_to_check:

                adj_fresh_oranges = getAdjFreshOranges(grid, rotten)
                for orange in adj_fresh_oranges:
                    # flip 1 -> 2
                    x = orange[0]
                    y= orange[1]
                    grid[x][y] = 2

                    fresh_oranges_set.remove(orange)
                    next_rotten_oranges.append(orange)

            rotten_oranges_to_check = next_rotten_oranges
            minutes += 1 if rotten_oranges_to_check else 0


        return minutes if not fresh_oranges_set else -1


if __name__ == '__main__':

    # # TEST 1
    # grid = [[2,1,1],[1,1,0],[0,1,1]]
    # sol = Solution()
    # for row in grid:
    #     print(row)
    # print("Test1: {}".format(sol.orangesRotting(grid)))
    #
    # # TEST 2
    # grid = [[2,1,1],[1,0,0],[0,0,1]]
    # sol = Solution()
    # for row in grid:
    #     print(row)
    # print("Test2: {}".format(sol.orangesRotting(grid)))
    #
    #
    # # TEST 3
    # grid = [[0,1],[1,1]]
    # sol = Solution()
    # for row in grid:
    #     print(row)
    # print("Test3: {}".format(sol.orangesRotting(grid)))
    #
    # # TEST 4
    # grid = [[2,0],[0,1]]
    # sol = Solution()
    # for row in grid:
    #     print(row)
    # print("Test4: {}".format(sol.orangesRotting(grid)))

    #
    # # TEST 5
    # grid = [[2,1],[0,1]]
    # sol = Solution()
    # for row in grid:
    #     print(row)
    # print("Test5: {}".format(sol.orangesRotting(grid)))
    #
    #
    # # TEST 6
    # grid = [[2,1,1],[1,1,0],[0,1,2]]
    # sol = Solution()
    # for row in grid:
    #     print(row)
    # print("Test6: {}".format(sol.orangesRotting(grid)))

    # TEST 7
    grid =  [[1,2]]
    sol = Solution()
    for row in grid:
        print(row)
    print("Test7: {}".format(sol.orangesRotting(grid)))



