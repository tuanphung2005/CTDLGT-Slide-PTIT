import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        num_test_cases = int(next(iterator))
        
        for _ in range(num_test_cases):
            n = int(next(iterator))
            a = []
            
            # Đọc n sợi dây
            for _ in range(n):
                a.append(int(next(iterator)))
            
            # Tạo Min-Heap từ mảng a
            heapq.heapify(a)
            
            total_cost = 0
            
            # Lặp cho đến khi chỉ còn 1 sợi dây duy nhất trong heap
            while len(a) > 1:
                # Lấy ra 2 sợi ngắn nhất
                first = heapq.heappop(a)
                second = heapq.heappop(a)
                
                # Chi phí nối
                current_cost = first + second
                total_cost += current_cost
                
                # Bỏ sợi dây mới tạo thành vào lại heap
                heapq.heappush(a, current_cost)
            
            print(total_cost)
            
    except StopIteration:
        pass

if __name__ == "__main__":
    solve()