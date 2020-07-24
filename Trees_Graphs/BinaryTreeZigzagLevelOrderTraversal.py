'''
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right
 to left for the next level and alternate between).


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root: return []


        s_odd  = []
        s_even = [root]

        result = [[]]
        level = 0

        change_level = False

        while s_odd or s_even:

            while s_odd:

                node = s_odd.pop()

                # add to result
                result[level].append(node.val)

                # add to stack
                if node.right:
                    s_even.append(node.right)
                if node.left:
                    s_even.append(node.left)

                change_level = True

            if change_level and s_even:
                result.append([])
                level += 1
                change_level = False

            while s_even:

                node = s_even.pop()

                # add to result
                result[level].append(node.val)

                if node.left:
                    s_odd.append(node.left)

                if node.right:
                    s_odd.append(node.right)

            result.append([])
            level += 1

        return result[:-1]







