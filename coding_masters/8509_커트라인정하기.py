tot, p = map(int, input().split())
score_list = list(map(int, input().split()))

max_score = 0
max_p = 0
for target in score_list:
    pass_list = [0] * tot
    for idx, score in enumerate(score_list):
        if target <= score:
            pass_list[idx] = 1
            if idx == 0: pass_list[idx + 1] = 1
            elif idx == (tot - 1): pass_list[idx - 1] = 1
            else:
                pass_list[idx - 1] = 1
                pass_list[idx + 1] = 1
    
    p_size = pass_list.count(1)  
    if max_score < target and p_size <= p and max_p < p_size:
        max_score = target
        max_p = pass_list.count(1)

if max_score != 0:
    print(max_score)
else:
    print(min(score_list) - 1)