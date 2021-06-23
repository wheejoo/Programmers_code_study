def solution(n,signs):
    for temp in range(n):
        for start in range(n):
            for end in range(n):
                if signs[start][temp] == 1 and signs[temp][end] == 1:
                    signs[start][end] = 1
    return signs
