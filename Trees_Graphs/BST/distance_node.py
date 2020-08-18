import os
import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.prev_root = None
        self.level = None 

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, x):
        path = []
        
        # Insert node into tree
        if not self.root:
            self.root = Node(x)
            self.root.level = 0
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
                    cur_node.right.prev_root = cur_node
                    cur_node.right.level = cur_node.level + 1
                    path.append(x)
                    return path
                else:
                    cur_node = cur_node.right
            else: # Go left
                if not cur_node.left:
                    cur_node.left = Node(x)
                    cur_node.left.prev_root = cur_node

                    # Whenever we insert, level increases
                    cur_node.left.level = cur_node.level + 1
                    path.append(x)
                    return path
                else:
                    cur_node = cur_node.left

    def in_order(self, root):
        if root:
            print(root.val)
            self.in_order(root.left)
            self.in_order(root.right)

    def traverse(self, val):
        cur_node = self.root

        while cur_node:
            # Go right
            if cur_node.val == val:
                return cur_node

            if val >= cur_node.val:
                cur_node = cur_node.right
            else: # Go left
                cur_node = cur_node.left

    def BFS(self, cur_node, end_node, visited=[]): 
  
        # Create a queue for BFS 
        queue = [] 
  
        # Traverse to first node's value
        cur_node = self.traverse(cur_node)

        # Mark the source node as visited and enqueue it 
        queue.append(cur_node) 
        visited[cur_node.val] = True
        distance = 0
        path = []
        level = []
  
        while queue: 
            # Dequeue a vertex from queue and print it 
            prev_node = cur_node
            cur_node = queue.pop(0) 
            path.append(cur_node.val)

            # Append level if we have not visited a level
            if cur_node.level not in level:
                level.append(cur_node.level)

                # Add here to avoid adding once we've reached our target node
                distance+=1

            if cur_node.val == end_node:
                return distance, path

            # Look at adjacent nodes (left, right, prev_root)
            # Left
            if cur_node.left and not visited[cur_node.left.val]:
                queue.append(cur_node.left)
                visited[cur_node.left.val] = True
                
            # Right
            if cur_node.right and not visited[cur_node.right.val]:
                queue.append(cur_node.right)
                visited[cur_node.right.val] = True

            # Prev_root
            if cur_node.prev_root and not visited[cur_node.prev_root.val]:
                queue.append(cur_node.prev_root)
                visited[cur_node.prev_root.val] = True

def main():
    # Examples
    unique_integers = [5, 6, 3, 4, 2, 1]
    unique_integers = [5, 3, 2, 4, 8, 6]
    unique_integers = [8, 3, 2, 1, 5, 4, 20, 25, 15, 10, 9, 13]
    node1 = 15 
    node2 = 4 
    
    paths = []

    # Create BST
    tree = BST()

    # Find max index to go to
    ind_1 = unique_integers.index(node1)
    ind_2 = unique_integers.index(node2)
    print(unique_integers[:max(ind_1, ind_2)+1])

    # Insert nodes only until the last needed node
    for num in unique_integers[:max(ind_1, ind_2)+1]:
        path = tree.insert(num)
        
        # Append two paths
        if num == node1 or num == node2:
            paths.append(path)

    """""""""""""""""""""""""""""""""""""""
                    BFS
    """""""""""""""""""""""""""""""""""""""
    # Mark all the vertices as not visited 
    visited = {num:False for num in unique_integers}
    distance, path = tree.BFS(node1, node2, visited)
    print(path)

    print(f"Distance between {node1} and {node2} is: {distance}") 
    """""""""""""""""""""""""""""""""""""""
    """""""""""""""""""""""""""""""""""""""

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
    # print(piece_1)
    # print(piece_2)
    overall_path = [*piece_1, *overall_path, *piece_2]
    print(f"Distance between {node1} and {node2} is: {len(overall_path)-1}") 


if __name__ == "__main__":
    main()
