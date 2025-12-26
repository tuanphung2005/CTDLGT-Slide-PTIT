class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(n, a, i):
    if i > n:
        return None
    root = Node(a[i - 1])
    root.left = build_tree(n, a, i * 2)
    root.right = build_tree(n, a, i * 2 + 1)

    return root

def in_order(node, res):
    if node is None:
        return
    in_order(node.left, res)
    res.append(str(node.val))
    in_order(node.right, res)


def solve(n, a):
    root = build_tree(n, a, 1)
    res = []
    in_order(root, res)
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(*solve(n, a))