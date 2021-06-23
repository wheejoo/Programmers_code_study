def solution(budgets, M):
    low = 1
    high = max(budgets)
    
    while low <= high:
        mid = (low + high) // 2
        total = sum([min(mid, budget) for budget in budgets])
        
        if M >= total:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1
