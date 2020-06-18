class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # While loop until no fresh apples are left
        # or we return earlier inside the loop

        # Start minute clock
        minute = 0

        def check_adj_fresh_orange(grid: List[List[int]], pos_orange):
            fresh_oranges_to_infect = []
            pos_orange = {'row': pos_orange[0], 'col': pos_orange[1]}

            # Check up and down of rotting orange

            # Not out of bounds on the up
            if (pos_orange['row'] - 1) >= 0:
                # Check up orange
                if grid[pos_orange['row']-1][pos_orange['col']] == 1:
                    # Append the up orange to infect next minute
                    fresh_oranges_to_infect.append((pos_orange['row']-1, pos_orange['col']))

            # Not out of bounds on the down
            if pos_orange['row'] + 1 < len(grid):
                # Check down orange
                if grid[pos_orange['row']+1][pos_orange['col']] == 1:
                    # Append the down orange to infect next minute
                    fresh_oranges_to_infect.append((pos_orange['row']+1, pos_orange['col']))

            # Check left and right of rotting orange

            # Not out of bounds left
            if pos_orange['col'] - 1 >= 0:
                # Check left orange
                if grid[pos_orange['row']][pos_orange['col']-1] == 1:
                    # Append the left orange to infect next minute
                    fresh_oranges_to_infect.append((pos_orange['row'], pos_orange['col']-1))

            # Not out of bounds right
            if pos_orange['col'] + 1 < len(grid[0]):
                # Check right orange
                if grid[pos_orange['row']][pos_orange['col']+1] == 1:
                    # Append the right orange to infect next minute
                    fresh_oranges_to_infect.append((pos_orange['row'], pos_orange['col']+1))

            return fresh_oranges_to_infect

        # Find number of infected oranges in the beginning
        num_before_infected_oranges = sum([1 for row in grid for orange in row if orange == 2])

        # While there are fresh oranges in the grid, keep going
        while any([any([oj for oj in row if oj == 1]) for row in grid]):
            # Start from rotting oranges and see which one it will infect next minute

            # Location of rotting oranges
            loc_rot_orange = [(row, col) for row, oranges_row in enumerate(grid) for col, orange in enumerate(oranges_row) if orange == 2]
            num_after_infected_oranges = len(loc_rot_orange)

            # If number of infected oranges does not increase then return -1
            if (num_before_infected_oranges == num_after_infected_oranges) and (minute != 0):
                return -1
            else:
                # Update number of before infected oranges
                num_before_infected_oranges = num_after_infected_oranges

            # Find all fresh oranges to infect next minute
            for rotting_orange in loc_rot_orange:
                fresh_oranges_to_infect = check_adj_fresh_orange(grid, rotting_orange)

                # Infect fresh oranges
                for row, col in fresh_oranges_to_infect:
                    grid[row][col] = 2

            # Increase minute clock
            minute += 1

        return minute
