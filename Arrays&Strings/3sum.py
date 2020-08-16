'''
https://leetcode.com/problems/3sum/
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?

Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''




# this solution works but it is too slow
class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def getPairs(sequence, target):

            remainder_map = {}
            result = []

            for i, number in enumerate(sequence):

                if number in remainder_map:
                    x = remainder_map[number]
                    result.append([sequence[x],number])

                else:

                    remainder_map[target - number] = i

            return result

        visited_triples = set()

        nums.sort() # O(nlogn)
        result = []

        for idx, num in enumerate(nums):

            target = (-1)*num

            list_of_pairs = getPairs(nums[idx+1:], target) # [] if no pairs found

            if list_of_pairs:

                for lst in list_of_pairs:
                    lst.append(num)

                clean_list = []

                for lst in list_of_pairs:
                    if tuple(lst) not in visited_triples:
                        clean_list.append(lst)
                        visited_triples.add(tuple(lst))

                result.extend(clean_list)

        return result




