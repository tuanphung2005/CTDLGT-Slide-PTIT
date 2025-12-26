import sys
from collections import Counter

def solve():
    # Đọc dữ liệu đầu vào
    try:
        # Cách đọc này an toàn hơn input() thường
        input_data = sys.stdin.read().split()
    except Exception:
        return

    if not input_data:
        return

    iterator = iter(input_data)
    try:
        t = int(next(iterator))
        for _ in range(t):
            s = next(iterator)
            n = len(s)
            
            # Đếm tần suất các ký tự
            counts = Counter(s)
            
            # Tìm số lần xuất hiện nhiều nhất
            # counts.most_common(1) trả về list kiểu [('a', 5)], ta lấy số 5
            max_freq = counts.most_common(1)[0][1]
            
            # Kiểm tra điều kiện
            if max_freq <= (n + 1) // 2:
                print(1)
            else:
                print(-1)
                
    except StopIteration:
        pass

if __name__ == "__main__":
    solve()