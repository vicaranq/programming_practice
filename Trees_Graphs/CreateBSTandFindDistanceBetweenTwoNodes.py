'''

input = [5, 3, 2, 4, 8, 6], 5 ,4
      5
    /   \
   3     8
  / \    /
2    4  6

output = 2

'''
import queue

class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

def addNode(node, val):

    if val >= node.val:
        if not node.right:
            node.right = Node(val)
        else:
            addNode(node.right, val)
    else:
        if not node.left:
            node.left = Node(val)
        else:
            addNode(node.left, val)



def bst(list_of_nodes):

    assert list_of_nodes
    root = Node(list_of_nodes[0])

    for node_val in list_of_nodes[1:]:
        addNode(root, node_val)

    return root

class llNode:

    def __init__(self, val, pos):
        self.val = val
        self.pos = pos
        self.next = None

def getNestedList(root):

    # assuming only one white space to the right or left but it depends on the number of children underneath

    q = queue.Queue()
    q.put((root, 0,  0)) # (node, row, col)
    nl = []

    left_most_pos = 0

    while not q.empty():
        node, level, width = q.get()

        if width < left_most_pos:
            left_most_pos = width

        lln = llNode(node.val, width)
        if level < len(nl):
            # nl[level].append(node)
            # lln = llNode(node.val, width)
            llnode = nl[level]
            while llnode.next:
                llnode = llnode.next
            llnode.next = lln
        else:
            # nl.append([node])
            nl.append(lln)

        if node.left:
            q.put((node.left, level+1, width - 1))
        if node.right:
            q.put((node.right, level+1, width + 1))

    return nl, left_most_pos



def print_bst(node):
    nested_list, left_most_pos = getNestedList(node)

    for llnode in nested_list:

        node = llnode
        while node:
            print("{} {}".format(node.val, node.pos))
            node = node.next

val_to_whiteSpaces = {}
def print_bst(node):
    helper(node)

    helper2(node)

def helper2(node):

    q = queue.Queue()
    curr_level = 0
    q.put((node,0))
    tmp_str = ""
    while not q.empty():
        n, level = q.get()

        left_white_spaces = val_to_whiteSpaces[n.val][0]
        right_white_spaces = val_to_whiteSpaces[n.val][1]

        if level != curr_level:
            tmp_str += "\n"
            curr_level = level

        tmp_str += " "*left_white_spaces + str(node.val) + " "*(right_white_spaces+1)

        if n.left:
            q.put((n.left, level + 1))
        if n.right:
            q.put((n.right, level + 1))




def helper(node):
    if not node:
        return 0

    left_spaces = helper(node.left)
    right_spaces = helper(node.right)
    val_to_whiteSpaces[node.val] = (left_spaces, right_spaces)

    return  left_spaces + 1 + right_spaces


def distanceBtwnNodes(root, n1, n2):
    # if map {node_vale : level} is constructed while creating the BST, we can have this calculated without traversing
    # the tree again

    # solution with out mapping
    def getDistancetoVal(node, val, l = 0):

        if not node:
            return -1 # val was not found
        if node.val == val:
            return l # val found

        if val >= node.val:
            return getDistancetoVal(node.right, val, l+1)
        else:
            return getDistancetoVal(node.left, val, l+1)

    def findnode(node, val):
        if not node:
            return -1
        if node.val == val:
            return node
        if val >= node.val:
            return findnode(node.right,val)
        else:
            return findnode(node.left,val)


    newRoot1 = findnode(root, n1)
    assert newRoot1 != -1

    distanceFrom1 = getDistancetoVal(newRoot1, n2)

    if distanceFrom1 == -1:
        newRoot2 = findnode(root, n2)
        distanceFrom2 = getDistancetoVal(newRoot2, n1)
    else:
        return distanceFrom1

    return distanceFrom2 if distanceFrom2 != -1 else None




inp = [5, 3, 2, 4, 8, 6]

root = bst(inp)
print_bst(root)

n1 = 8
n2 = 2
print("Distance between {} and {} is: {}".format(n1, n2, distanceBtwnNodes(root, n1, n2)))
