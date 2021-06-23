def solution(l, v):
    v.sort()
    answer = []
   
    #시작점
    if 0 not in v:
        answer.append(v[0])
    #끝점
    if l not in v:
        answer.append(l-v[-1])
        
    for x,y in zip(v[1:], v[:-1]):
        if (x-y) % 2 == 0:
            d = (x-y) // 2
        else:
            d = (x-y) // 2 + 1
        answer.append(d)
    return max(answer)
