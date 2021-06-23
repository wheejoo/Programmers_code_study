from itertools import combinations
def solution(m, weights):
    answer = 0
    for cnt in range(1,len(weights)):
        total = map(sum, combinations(weights,cnt))
        for t in total:
            if t == m:
                answer += 1
    return answer
