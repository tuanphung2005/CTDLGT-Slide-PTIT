class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

def build(values):
    if not values:
        return None
    head = Node(values[0])
    cur = head
    for v in values[1:]:
        cur.next = Node(v)
        cur = cur.next
    return head

def xoa(head):
    seen = set()
    dummy = Node(0, head)
    prev, cur = dummy, head
    while cur:
        if cur.val in seen:
            prev.next = cur.next
            cur = cur.next
        else:
            seen.add(cur.val)
            prev = cur
            cur = cur.next
    return dummy.next

def res(head):
    res = []
    cur = head
    while cur:
        res.append(str(cur.val))
        cur = cur.next
    print(" ".join(res))

n = int(input())
vals = list(map(int, input().split()))
head = build(vals)
head = xoa(head)
res(head)