import sys

def solve():
    # Đọc dữ liệu an toàn (xử lý cả trường hợp nhiều dòng)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    weights = [int(x) for x in input_data]
    
    # Biến lưu kết quả tốt nhất (khởi tạo vô cùng lớn)
    min_diff = float('inf')
    
    # Mảng lưu tổng cân nặng 4 nhóm
    group_sums = [0] * 4
    # Mảng đếm số người trong 4 nhóm
    group_counts = [0] * 4
    
    def backtrack(index):
        nonlocal min_diff
        
        # Nếu đã xếp xong 12 người
        if index == 12:
            current_diff = max(group_sums) - min(group_sums)
            if current_diff < min_diff:
                min_diff = current_diff
            return

        # Nhánh cận: Nếu chênh lệch hiện tại (sơ bộ) đã lớn hơn min_diff tìm được
        # thì có thể cắt tỉa (Tuy nhiên với N=12 thì không bắt buộc cần bước này vẫn AC)
        
        # Thử xếp người thứ 'index' vào 1 trong 4 nhóm
        for i in range(4):
            if group_counts[i] < 3:
                # Tối ưu đối xứng: 
                # Nếu nhóm hiện tại đang trống (sum=0), thì việc xếp vào nhóm trống này
                # hay nhóm trống tiếp theo là như nhau. Chỉ cần xếp vào nhóm trống đầu tiên tìm thấy.
                if group_counts[i] == 0:
                    # Logic: Nếu nhóm i trống, ta bỏ vào đây và KHÔNG cần thử các nhóm j > i trống khác nữa
                    # để tránh hoán vị lặp lại không cần thiết.
                    group_sums[i] += weights[index]
                    group_counts[i] += 1
                    backtrack(index + 1)
                    group_counts[i] -= 1
                    group_sums[i] -= weights[index]
                    break 
                else:
                    # Nhóm không trống, thử bình thường
                    group_sums[i] += weights[index]
                    group_counts[i] += 1
                    backtrack(index + 1)
                    group_counts[i] -= 1
                    group_sums[i] -= weights[index]

    # Mẹo nhỏ: Sắp xếp giảm dần giúp các nhánh cận hoạt động tốt hơn (nếu có)
    weights.sort(reverse=True)
    backtrack(0)
    print(min_diff)

if __name__ == "__main__":
    solve()