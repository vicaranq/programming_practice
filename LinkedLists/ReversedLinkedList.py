'''
https://leetcode.com/problems/reverse-linked-list/

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        return recursive(head, None)

def recursive(node, prev_node):

    if not node:
        return prev_node

    # save next node
    next_node = node.next

    # relinked node
    node.next = prev_node
    return recursive(next_node, node)







