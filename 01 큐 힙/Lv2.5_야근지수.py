import heapq
def solution(n, works):
    if n > sum(works):
        return 0
    work = [(-i,i) for i in works]
    heapq.heapify(work)
    for _ in range(n):
        w = heapq.heappop(work)[1]-1
        heapq.heappush(work,(-w,w))
    answer = sum([i[1]**2 for i in work])
    return answer
