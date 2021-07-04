import math
from itertools import permutations
def check(n):
    if n < 2:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
            return True
def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        arr = list(permutations(numbers,i))
        for j in range(len(arr)):
            num = int(''.join(map(str,arr[j])))
            if check(num):
                answer.append(num)
    answer = list(set(answer))
    return len(answer)
