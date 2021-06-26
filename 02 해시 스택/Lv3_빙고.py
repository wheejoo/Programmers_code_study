def solution(board, nums):
    N = len(board)
    row_bingo_counts = [0] * N
    col_bingo_counts = [0] * N
    diagonal_bingo_counts = [0] * 2
    
    num = set(nums)
    for i,row in enumerate(board):
        for j,num in enumerate(row):
            if num in nums:
                row_bingo_counts[i] += 1
                col_bingo_counts[j] += 1
                
                if i == j:
                    diagonal_bingo_counts[0] += 1
                if i + j == N - 1:
                    diagonal_bingo_counts[1] += 1
    return (row_bingo_counts + col_bingo_counts + diagonal_bingo_counts).count(N)
