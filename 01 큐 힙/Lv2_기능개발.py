def solution(progresses, speeds):
    answer = []
    x = 0
    while len(progresses) != x:
        tmp = 0
        for i in range(x,len(progresses)):
            progresses[i] += speeds[i]
            
        if progresses[x] >= 100:
            for i in range(x,len(progresses)):
                if progresses[i] >= 100:
                    tmp += 1
                else:
                    break
            answer.append(tmp)
            x += tmp
    return answer
