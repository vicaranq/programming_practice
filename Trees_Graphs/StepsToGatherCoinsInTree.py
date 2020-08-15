

class Node:
    def __init__(self, hasCoin):
        self.hasCoin = hasCoin
        self.children = []

# create tree
A = Node(False)
B = Node(False)
C = Node(False)
D = Node(True)
E = Node(True)
F = Node(False)
G = Node(False)

A.children = [B, C, D]
B.children = [E, F]
D.children = [G]

def rec(node):
    if not node:
        return 0
    steps = 0

    for child in node.children:
        steps += rec(child)

    return 1 + steps if node.hasCoin or steps > 0 else 0




def stepsToGetCoins(root):
    return (rec(root)-1)*2



print(stepsToGetCoins(A))







