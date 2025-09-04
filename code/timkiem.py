class Student:
    def __init__(self, sid, name, score):
        self.id = sid
        self.name = name
        self.score = score

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, score: {self.score}"


def tuantu(students, x):
    for sv in range(len(students)):
        if students[sv].score == x:
            return students[sv]
    return None

def nhiphan(students, x):
    left, right = 0, len(students) - 1
    while left <= right:
        mid = (left + right) // 2
        if students[mid].score == x:
            return students[mid]
        elif students[mid].score < x:
            left = mid + 1
        else:
            right = mid - 1
    return None

def tamphan(students, left, right, x):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if students[mid1].score == x:
            return students[mid1]
        if students[mid2].score == x:
            return students[mid2]

        if x < students[mid1].score:
            return tamphan(students, left, mid1 - 1, x)
        elif x > students[mid2].score:
            return tamphan(students, mid2 + 1, right, x)
        else:
            return tamphan(students, mid1 + 1, mid2 - 1, x)
    return None

def search(sv):
    return sv if sv else "khong tim thay"

T = int(input("so luong sinh vien: "))

students = []
sid = 1
for i in range(T):
    # sid = input(f"id sinh vien {i+1}: ")
    sid += 1
    name = input(f"ten sinh vien so {i+1}: ")
    score = float(input(f"diem sinh vien so {i+1}: "))
    students.append(Student(sid, name, score))

x = float(input("\ndiem so can tim: "))

print("\ntim kiem tuan tu")
sv = tuantu(students, x)
print(search(sv))

students = sorted(students, key=lambda s: s.score)

print("\ntim kiem nhi phan")
sv = nhiphan(students, x)
print(search(sv))

print("\ntim kiem tam phan")
sv = tamphan(students, 0, len(students) - 1, x)
print(search(sv))