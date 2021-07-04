def solution(clothes):
    d = {}
    for x,y in clothes:
        d[y] = d.get(y,0) + 1
    answer = 1
    for v in d.values():
        answer *= (v+1)
    return answer-1
