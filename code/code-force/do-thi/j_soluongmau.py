import sys

# Tăng tốc độ đọc dữ liệu
input = sys.stdin.read().split()

def solve():
    if not input: return
    n = int(input[0])
    q = int(input[1])
    
    # Màu của các đỉnh (chuyển về index từ 0)
    colors = list(map(int, input[2:n+2]))
    
    # Cấu trúc DSU
    parent = list(range(n))
    # counts[i] lưu Dictionary màu của bang mà i là đại diện
    counts = [{colors[i]: 1} for i in range(n)]

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i]) # Path compression
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            # Kỹ thuật Small-to-Large: Gộp thằng ít màu hơn vào thằng nhiều màu hơn
            if len(counts[root_i]) < len(counts[root_j]):
                root_i, root_j = root_j, root_i
            
            # Đổi cha
            parent[root_j] = root_i
            
            # Gộp Dictionary màu từ root_j sang root_i
            for color, amount in counts[root_j].items():
                counts[root_i][color] = counts[root_i].get(color, 0) + amount
            
            # Xóa dữ liệu cũ để tiết kiệm bộ nhớ
            counts[root_j] = {}

    ptr = n + 2
    results = []
    for _ in range(q):
        t = int(input[ptr])
        x = int(input[ptr+1]) - 1 # Chuyển về index 0
        y = int(input[ptr+2])
        ptr += 3
        
        if t == 1:
            union(x, y-1) # y ở đây là đỉnh y trong truy vấn 1
        else:
            root = find(x)
            # Truy vấn loại 2: y là mã màu cần tìm
            results.append(str(counts[root].get(y, 0)))

    sys.stdout.write("\n".join(results) + "\n")

solve()