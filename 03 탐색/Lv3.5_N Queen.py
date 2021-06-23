def solution(n):
    columns = set()
    diagonals1 = set()
    diagonals2 = set()
    return dfs(n,0,columns,diagonals1,diagonals2)

def dfs(n,row,columns,diagonals1,diagonals2):
    if row == n:
        return 1
    answer = 0
    for col in range(n):
        if col in columns or (row+col) in diagonals1 or (row-col) in diagonals2:
            continue
        columns.add(col)
        diagonals1.add(row+col)
        diagonals2.add(row-col)
        answer += dfs(n,row+1,columns,diagonals1,diagonals2)
        
        columns.remove(col)
        diagonals1.remove(row+col)
        diagonals2.remove(row-col)
    return answer
