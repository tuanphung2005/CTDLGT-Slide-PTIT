def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve():
    T = int(input().strip())
    
    for _ in range(T):
        n = int(input().strip())
        edges = input().split()
        
        ke = {}
        con = set()
        all_node = set()

        for i in range(0, len(edges), 3):
            u = int(edges[i])
            v = int(edges[i+1])
            huong = edges[i+2]
            
            if u not in ke:
                ke[u] = {}
            
            if huong == 'L':
                ke[u]['L'] = v
            else:
                ke[u]['R'] = v
            
            con.add(v)
            all_node.add(u)
            all_node.add(v)
            
        root = None
        for node in all_node:
            if node not in con:
                root = node
                break
        
        max = 0
        stack = [(root, 1 if is_prime(root) else 0)]
        
        while stack:
            u, count = stack.pop()
            has_left = u in ke and 'L' in ke[u]
            has_right = u in ke and 'R' in ke[u]
            
            if not has_left and not has_right:
                if count > max:
                    max = count
                continue
            if has_right:
                v_right = ke[u]['R']
                stack.append((v_right, count + (1 if is_prime(v_right) else 0)))
            if has_left:
                v_left = ke[u]['L']
                stack.append((v_left, count + (1 if is_prime(v_left) else 0)))
                
        print(max)

solve()