'''
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy_root = ListNode(-1)

        n1, n2 = (l1, l2)
        carry = 0
        prev_node = dummy_root

        while n1 or n2:

            # get sum and carry
            sm = carry
            sm += n1.val if n1 else 0
            sm += n2.val if n2 else 0

            carry = sm // 10
            val = sm % 10

            # create new node
            nn = ListNode(val)

            # assign new noded to previous, and update previous
            prev_node.next = nn
            prev_node = prev_node.next

            # update n1 and n2
            n1 = n1.next if n1 else None
            n2 = n2.next if n2 else None

        # check carry
        if carry:
            nn = ListNode(1)
            prev_node.next = nn

        return dummy_root.next

