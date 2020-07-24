

'''
https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.



# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
'''

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head:
            return None

        id_to_newNode_map = {}

        def recursive(node):

            if not node:
                return None

            new_node = Node(node.val)

            id_to_newNode_map[id(node)] = new_node

            new_node.next = recursive(node.next)
            new_node.random = id_to_newNode_map[id(node.random)] if node.random else None

            return new_node

        head_copy =  recursive(head)

        return head_copy


