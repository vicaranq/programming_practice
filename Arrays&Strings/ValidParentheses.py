'''
https://leetcode.com/problems/valid-parentheses/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

'''

class Solution:
    def isValid(self, s: str) -> bool:


        open_stack = []

        close_to_open_map = { ')': '(', ']':'[','}':'{'}

        open_set = set(['(','[','{'])

        for char in s:

            if char in open_set:
                open_stack.append(char)
            else:
                assert char in close_to_open_map, "Unexpected closing character"

                if not open_stack:
                    return False

                prev_open = open_stack.pop()

                if prev_open != close_to_open_map[char]:
                    return False

        return True if not open_stack else False




