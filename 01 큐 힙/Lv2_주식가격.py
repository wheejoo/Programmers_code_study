from collections import deque
def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        price = q.popleft()
        time = 0
        for n in q:
            time += 1
            if n < price:
                break
        answer.append(time)
    return answer
