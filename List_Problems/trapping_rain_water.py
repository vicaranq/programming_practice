'''
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
is able to trap after raining.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

'''

class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: return 0

        L = 0
        R = len(height) - 1

        highest_left = height[L]
        highest_right = height[R]

        left_height = height[L]
        right_height = height[R]

        result = 0

        while L < R:

            if highest_left <= highest_right:
                # move left pivot
                if left_height < highest_left:
                    result += highest_left - left_height
                L += 1
                left_height = height[L]
                highest_left  = left_height  if left_height > highest_left else highest_left

            else:
                #move right pivot

                if right_height < highest_right:

                    result += highest_right-right_height

                R -= 1
                right_height = height[R]
                highest_right = right_height if right_height > highest_right else highest_right

        return result

