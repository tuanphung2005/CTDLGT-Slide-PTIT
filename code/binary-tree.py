from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def in_order_dfs(node):
    if node is None:
        return
    in_order_dfs(node.left)
    print(node.value)
    in_order_dfs(node.right)

def insert(root, key):
    if root is None:
        return Node(key)
    queue = deque([root])
    while queue:
        temp = queue.popleft()
        if temp.left is None:
            temp.left = Node(key)
            break
        else:
            queue.append(temp.left)
        if temp.right is None:
            temp.right = Node(key)
            break
        else:
            queue.append(temp.right)

    return root

T = int(input())
for _ in range(T):
    n = int(input())
    root = None
    values = list(map(int, input().split()))
    for i in values:
        root = insert(root, i)
    in_order_dfs(root)
