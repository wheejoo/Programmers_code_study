def solution(s):
    answer = []
    for i in s:
        while answer and answer[-1] < i:
            answer.pop()
        answer.append(i)
    return ''.join(answer)
