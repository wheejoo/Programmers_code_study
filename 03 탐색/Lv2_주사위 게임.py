def solution(monster, S1, S2, S3):
    answer = -1
    s1_list = list(range(1,S1+1))
    s2_list = list(range(1,S2+1))
    s3_list = list(range(1,S3+1))
    total_list = []
    
    for s1 in s1_list:
        for s2 in s2_list:
            for s3 in s3_list:
                total_list.append((s1+s2+s3+1))
                
    cnt = 0
    for pos in total_list:
        if pos in monster:
            cnt += 1
            
    answer = (len(total_list) - cnt) / len(total_list) * 1000
    return int(answer)
