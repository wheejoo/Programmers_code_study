def solution(citations):
    citations.sort()
    num = len(citations)
    for i in range(num):
        if citations[i] >= num - i:
            return num - i
    answer = 0
    return answer
