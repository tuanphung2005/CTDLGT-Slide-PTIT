import sys

def solve():
    # Đọc dữ liệu đầu vào
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        num_test_cases = int(next(iterator))
    except StopIteration:
        return

    for _ in range(num_test_cases):
        try:
            a = int(next(iterator))
            b = int(next(iterator))
            c = int(next(iterator))
        except StopIteration:
            break

        # Tìm kiếm nhị phân trên tập số thực
        low = 0.0
        # Cận trên an toàn. Vì A*x^3 + B*x = C và A,B >= 1, 
        # nên x chắc chắn nhỏ hơn C (với C >= 1) hoặc nhỏ hơn 100.
        # Chọn 1000.0 cho dư dả vì C <= 1000.
        high = 1000.0 

        # Lặp 100 lần để đạt độ chính xác cao
        for _ in range(100):
            mid = (low + high) / 2
            val = a * (mid ** 3) + b * mid
            
            if val > c:
                high = mid  # Giá trị quá lớn, giảm cận trên
            else:
                low = mid   # Giá trị quá nhỏ, tăng cận dưới
        
        # In kết quả lấy 4 chữ số sau dấu phẩy
        print(f"{low:.4f}")

if __name__ == "__main__":
    solve()