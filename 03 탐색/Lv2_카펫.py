import math
def solution(brown, red):
    for i in range(1, int(math.sqrt(red)+1)):
        if red % i == 0:
            row, col = i, red//i
            if ((row+2)*2+(col*2)) == brown:
                return [col+2, row+2]
