class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root

def right_level_order(root):
    if root is None:
        return
    
    queue = [root]
    res = []
    while queue:
        current = queue.pop(0)
        res.append(str(current.val))

        if current.right:
            queue.append(current.right)
        if current.left:
            queue.append(current.left)

    print (*res)

def solve(n, a):
    root = a[0]
    root = Node(root)

    for i in range(1, n):
        insert(root, a[i])
    right_level_order(root)

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    solve(n, a)