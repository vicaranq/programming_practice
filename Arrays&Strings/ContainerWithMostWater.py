
'''
source:
https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

'''
class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        max_level= 0

        max_area = 0

        while right > left:

            left_height = height[left]
            right_height = height[right]

            temp_area = (right - left) * min(left_height, right_height)

            if temp_area > max_area:
                max_area = temp_area
                max_level = min(left_height, right_height)

            # move pivots
            if left_height <= right_height:
                left += 1

            else:
                right -= 1

        return max_area


