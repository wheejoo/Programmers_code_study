from itertools import combinations
import math
def solution(n):
    answer = 0
    s = [True] * n
    for i in range(2,int(math.sqrt(n)+1)):
        if s[i]:
            for j in range(i+i,n,i):
                s[j] = False
    prime = [i for i in range(2,n) if s[i]]
    result = list(combinations(prime,3))
    for r in result:
        if sum(r) == n:
            answer += 1
    return answer
