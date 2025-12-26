from itertools import combinations

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
        
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

N, K = map(int, input().split())

numbers = range(1, N + 1)

index = 1

for combo in combinations(numbers, K):
    if is_prime(index):

        combo_str = " ".join(map(str, combo))
        print(f"{index}: {combo_str}")
        
    index += 1