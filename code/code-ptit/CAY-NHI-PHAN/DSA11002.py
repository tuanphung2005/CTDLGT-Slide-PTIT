class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def build_tree(n, a, i):
    if i > n: return None
    root = Node(a[i - 1])
    root.left = build_tree(n, a, i * 2)
    root.right = build_tree(n, a, i * 2 + 1)
    return root

def cal(root):
    if root.left is None and root.right is None:
        return int(root.val)
    
    left = cal(root.left)
    right = cal(root.right)

    if root.val == "+": return left + right
    if root.val == "-": return left - right
    if root.val == "*": return left * right
    if root.val == "/": return left // right

    return 0

def solve(n, s):
    root = build_tree(n, s, 1)
    print(cal(root))

# solve(7, ['+', '*', '-', '5', '4', '100', '20'])
t = int(input())
for _ in range(t):

    n = int(input())
    s = input().split()
    solve(n, s)