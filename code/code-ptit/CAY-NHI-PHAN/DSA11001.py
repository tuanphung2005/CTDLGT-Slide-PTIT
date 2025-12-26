class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_operator(c):
    return c in "+-*/"

def inorder(root, res):
    if root is None:
        return

    inorder(root.left, res)
    res.append(root.val)
    inorder(root.right, res)

def solve(P):
    stack = []

    for c in P:
        if not is_operator(c):
            stack.append(Node(c))
        else:
            right = stack.pop()
            left = stack.pop()

            node.left = left
            node.right = right

            node = Node(c)

            stack.append(node)

    root = stack.pop()
    res = []
    inorder(root, res)
    return " ".join(res)
    
T = int(input())
for _ in range(T):
    P = input().strip()
    print(solve(P))
