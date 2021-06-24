def solution(s):
    stack = []
    open_chr = {'(':0, '{':1, '[':2}
    close_chr = {')':0, '}':1, ']':2}
    chr_idx = 0
    
    for chr in s:
        if chr in open_chr:
            chr_idx = open_chr[chr]
        elif chr in close_chr:
            chr_idx = close_chr[chr]
            
        if len(stack) == 0 and chr in close_chr:
            return False
        elif chr in open_chr:
            stack.append(chr_idx)
        else:
            if stack[-1] == close_chr[chr]:
                stack.pop()
            else:
                stack.append(chr_idx)
                
    if len(stack) == 0:
        return True
    else:
        return False
    # answer = True
    # return answer
