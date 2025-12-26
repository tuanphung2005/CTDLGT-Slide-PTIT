from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def build_tree(nodes):
    if not nodes or nodes == "N":
        return None
    root = Node(nodes[0])
    queue = deque([root])
    i = 1
    while queue and i < len(nodes):
        curr = queue.popleft()
        
        if i < len(nodes):
            if nodes[i] != 'N':
                curr.left = Node(nodes[i])
                queue.append(curr.left)
            i += 1
        if i < len(nodes):
            if nodes[i] != 'N':
                curr.right = Node(nodes[i])
                queue.append(curr.right)
            i += 1
    return root
def duyet_rnl(root, res):
    if root:
        duyet_rnl(root.right, res)
        res.append(root.value)
        duyet_rnl(root.left, res)
        
def solve(s):
    root = build_tree(s)
    res = []
    duyet_rnl(root, res)
    res.append('')
    return res

n = int(input())
for _ in range(n):
    s = input().split()
    print(*solve(s))