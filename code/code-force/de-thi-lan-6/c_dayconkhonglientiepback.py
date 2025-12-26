import sys
from collections import deque

def solve():
    # Đọc dữ liệu nhanh
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    
    # Chuyển đổi dữ liệu sang list số nguyên
    a = []
    for i in range(n):
        a.append(int(input_data[2 + i]))
        
    total_sum = sum(a)
    
    # DP[i] = Tổng bỏ đi nhỏ nhất nếu bỏ phần tử i
    dp = [0] * n
    
    # Deque lưu trữ các chỉ số j sao cho DP[j] tăng dần (Monotonic Queue)
    # Phần tử đầu tiên của deque luôn là chỉ số có DP nhỏ nhất trong cửa sổ hiện tại
    dq = deque()
    
    for i in range(n):
        # 1. Loại bỏ các chỉ số đã trượt ra khỏi cửa sổ (khoảng cách > K)
        # Chỉ số j hợp lệ phải thỏa mãn: i - K <= j < i
        while dq and dq[0] < i - k:
            dq.popleft()
            
        # 2. Tìm min DP trước đó
        # Nếu i < k, ta có thể bỏ a[i] ngay từ đầu mà không cần số bỏ trước đó
        prev_min = 0
        if dq:
            prev_min = dp[dq[0]]
            # Nếu i < k, ta so sánh việc nối tiếp từ dq[0] hoặc bắt đầu mới từ 0
            # Tuy nhiên theo logic min-queue, ta chỉ cần set prev_min = 0 nếu i < k
            # để đảm bảo tính đúng đắn, ta sửa logic một chút:
        
        if i < k:
            dp[i] = a[i]
        else:
            dp[i] = a[i] + prev_min
            
        # 3. Cập nhật Deque để duy trì tính đơn điệu tăng
        # Loại bỏ các phần tử ở cuối deque có giá trị DP lớn hơn DP[i] hiện tại
        # vì DP[i] mới hơn và nhỏ hơn, nên các phần tử kia sẽ không bao giờ được chọn nữa
        while dq and dp[dq[-1]] >= dp[i]:
            dq.pop()
            
        dq.append(i)
        
    # Kết quả là Total Sum - Min(các DP ở K phần tử cuối cùng)
    # Vì để phủ kín dãy số, lần bỏ cuối cùng phải nằm trong phạm vi K phần tử cuối
    min_discard = min(dp[n-k:])
    
    print(total_sum - min_discard)

if __name__ == "__main__":
    solve()