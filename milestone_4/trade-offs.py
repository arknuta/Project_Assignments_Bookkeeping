from typing import List, Tuple 

def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    for i in range(len(li)):
        for x in range(i + 1, len(li)):
            if li[i] + li[x] == target:
                return i, x



assert find_sum(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}

 # Time complexity: O(n^2) 


def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
    num_indices = {}
    for i, num in enumerate(li):
        complement = target - num
        if complement in num_indices:
            return num_indices[complement], i

        num_indices[num] = i

assert find_sum_fast(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}
# Time complexity: O(n)