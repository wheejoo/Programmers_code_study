def solution(answers):
    answer = []
    t_answer = []
    c1,c2,c3 = 0,0,0
    
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == one[i%len(one)]:
            c1 +=1 
        if answers[i] == two[i%len(two)]:
            c2 +=1 
        if answers[i] == three[i%len(three)]:
            c3 +=1 
    t_answer = [c1,c2,c3]
    
    for person, score in enumerate(t_answer):
        if score == max(t_answer):
            answer.append(person+1)
    return answer
