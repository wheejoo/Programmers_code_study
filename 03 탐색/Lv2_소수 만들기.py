from itertools import combinations
import math
def solution(nums):
    answer = 0
    num = combinations(nums,3)
    for item in num:
        s = sum(item)
        is_prime = True
        for i in range(2, int(math.sqrt(s))+1):
            if s % i == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1
    return answer
