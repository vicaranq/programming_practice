'''
https://leetcode.com/problems/valid-palindrome/
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:

        L = 0
        R = len(s) - 1

        s = s.lower()

        while L < R:

            while L < len(s) and not s[L].isalnum():
                L += 1

            while R >= 0 and not s[R].isalnum():
                R -= 1

            if L >= len(s) or R < 0:
                break

            if s[L] != s[R]:
                return False
            L += 1
            R -= 1


        return True
