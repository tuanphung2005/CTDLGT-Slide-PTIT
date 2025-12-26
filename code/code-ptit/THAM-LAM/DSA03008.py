import sys

def solve():
    # Đọc dữ liệu nhanh
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        # Đọc số bộ test
        t = int(next(iterator))
        
        for _ in range(t):
            n = int(next(iterator))
            
            # Đọc mảng Start
            starts = []
            for _ in range(n):
                starts.append(int(next(iterator)))
                
            # Đọc mảng Finish
            finishes = []
            for _ in range(n):
                finishes.append(int(next(iterator)))
            
            # Ghép thành danh sách các cặp (start, finish)
            activities = []
            for i in range(n):
                activities.append((starts[i], finishes[i]))
            
            # Sắp xếp theo thời gian kết thúc (Finish time) tăng dần
            # Nếu finish bằng nhau, thứ tự start không quá quan trọng cho bài toán đếm
            activities.sort(key=lambda x: x[1])
            
            count = 0
            last_finish_time = -1
            
            for s, f in activities:
                # Nếu thời gian bắt đầu của việc hiện tại >= thời gian kết thúc việc trước
                if s >= last_finish_time:
                    count += 1
                    last_finish_time = f
            
            print(count)
            
    except StopIteration:
        pass

if __name__ == "__main__":
    solve()