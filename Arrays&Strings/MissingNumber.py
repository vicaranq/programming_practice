'''
soruce: https://leetcode.com/problems/missing-number/
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return int(len(nums)*(len(nums)+1) / 2- sum(nums))

        # option 2
        # n = len(nums)
        # return int(n*(n+1) / 2 -sum(nums))

        # option 3
#         # find overall sum
#         n = len(nums)
#         total_sum = n*(n+1) / 2

#         # loop through numbers and subtract from total sum
#         for num in nums:
#             total_sum -= num

#         return int(total_sum)

