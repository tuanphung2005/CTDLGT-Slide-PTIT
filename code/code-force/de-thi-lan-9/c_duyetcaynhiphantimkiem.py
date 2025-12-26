class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def pre_order(root, res):
    if root:
        res.append(str(root.val))
        pre_order(root.left, res)
        pre_order(root.right, res)
        

def insert_node(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert_node(root.left, val)
    else: 
        root.right = insert_node(root.right, val)
    return root
    
def solve(n, a):
    root = None
    for val in a:
        root = insert_node(root, val)
        
    res = []
    pre_order(root, res)
    res.append('')
    return res
    
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res = solve(n, a)
    print(*res)
    
    