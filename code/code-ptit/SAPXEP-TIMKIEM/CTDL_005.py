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

def delete(head, x):
    dummy = Node(0, head)
    prev, cur = dummy, head
    count = 0
    while cur:
        if cur.val == x:
            prev.next = cur.next
            count += 1
            cur = cur.next
        else:
            prev = cur
            cur = cur.next
    return dummy.next, count

def res(head):
    res = []
    cur = head
    while cur:
        res.append(str(cur.val))
        cur = cur.next
    print(" ".join(res))

if __name__ == "__main__":
    n = int(input())
    vals = list(map(int, input().split()))
    x = int(input())
    head = build(vals)
    head, deleted = delete(head, x)
    res(head)