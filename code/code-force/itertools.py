from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

nums = [1, 2, 4, 5]
print('HOAN VI')
print(list(permutations(nums)))
print('TO HOP')
print(list(combinations(nums, 2)))
print('TO HOP CO LAP')
print(list(combinations_with_replacement(nums, 2)))