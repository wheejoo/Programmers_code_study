def solution(dirs):
    visited_path = set()
    DELTAS = {'U':(1,0), 'D':(-1,0), 'R':(0,1), 'L':(0,-1)}
    cur_pos = (0,0)
    
    for dir in dirs:
        dx,dy = DELTAS[dir]
        next_pos = (cur_pos[0]+dx, cur_pos[1]+dy)
        
        if not (-5<= next_pos[0] <= 5 and -5<= next_pos[1] <= 5):
            continue
            
        visited_path.add((cur_pos, next_pos))
        visited_path.add((next_pos, cur_pos))
            
        cur_pos = next_pos
    return len(visited_path)//2
