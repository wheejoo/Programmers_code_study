def solution(v):
    x = [0] * 4
    y = [0] * 4
    
    for i in range(0,3):
        x[i] = v[i][0]
        y[i] = v[i][1]
        
    for z in range(0,3):
        if x.count(x[z]) == 1:
            x[3] = x[z]
        if y.count(y[z]) == 1:
            y[3] = y[z]
    answer = [x[3],y[3]]
    return answer
