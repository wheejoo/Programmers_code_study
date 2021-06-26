def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        current = [chr for chr in i if chr in skill]
        b = True
        for x,y in zip(current,skill):
            if x != y :
                b = False
                break
        if b == True:
            answer += 1
    return answer
