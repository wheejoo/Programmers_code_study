def solution(s):
    answer = []
    if s.count('(') != s.count(')'):
        return False
    for ch in s:
        if ch == '(':
            answer.append(ch)
        else:
            if len(answer) == 0:
                return False
            answer.pop()
    return True
