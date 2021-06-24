def solution(seat):
    answer = set()
    for x,y in seat:
        if (x,y) not in answer:
            answer.add((x,y))
        else:
            continue
    return len(answer)
