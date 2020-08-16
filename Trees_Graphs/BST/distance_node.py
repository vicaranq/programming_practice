import os
import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.prev_root = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, x):
        path = []
        
        # Insert node into tree
        if not self.root:
            self.root = Node(x)
            path.append(x)
            return path

        # Start traversal
        cur_node = self.root

        while cur_node:
            path.append(cur_node.val)

            # Go right
            if x >= cur_node.val:
                # Create node on the right
                if not cur_node.right:
                    cur_node.right = Node(x)
                    cur_node.prev_root = cur_node
                    path.append(x)
                    return path
                else:
                    cur_node = cur_node.right
            else: # Go left
                if not cur_node.left:
                    cur_node.left = Node(x)
                    cur_node.prev_root = cur_node
                    path.append(x)
                    return path
                else:
                    cur_node = cur_node.left

    def in_order(self, root):
        if root:
            print(root.val)
            self.in_order(root.left)
            self.in_order(root.right)

def main():
    unique_integers = [5, 6, 3, 4, 2, 1]
    unique_integers = [5, 3, 2, 4, 8, 6]
    node1 = 8 
    node2 = 2 
    
    paths = []

    # Create BST
    tree = BST()

    # Find max index to go to
    ind_1 = unique_integers.index(node1)
    ind_2 = unique_integers.index(node2)

    # Insert nodes only until the last needed node
    for num in unique_integers[:max(ind_1, ind_2)+1]:
        path = tree.insert(num)
        
        # Append two paths
        if num == node1 or num == node2:
            paths.append(path)

    # Find distance
    overall_path = []

    for i, tup_path in enumerate(zip(*paths)):
        # If overlapping paths, update the last overlapping node
        if tup_path[0] == tup_path[1]: 
            last_overlapping_node = i
    else:
        overall_path.append(paths[0][last_overlapping_node])

    piece_1 = paths[0][last_overlapping_node+1:]
    piece_2 = paths[1][last_overlapping_node+1:]
    print(piece_1)
    print(piece_2)
    overall_path = [*piece_1, *overall_path, *piece_2]
    print(f"Distance between {node1} and {node2} is: {len(overall_path)-1}") 


if __name__ == "__main__":
    main()
