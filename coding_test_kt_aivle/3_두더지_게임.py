from collections import Counter

def solution(n, m, moles):
    moles.sort(key=lambda x:x[0])

    # 가장 많이 나오는 구멍 찾기
    freq_cnt = [0] * (n + 1)
    for time, idx, score in moles: freq_cnt[idx] += 1
    freq_cnt += freq_cnt[1:m]
    
    target, max_tot = [], 0
    for i in range(1, n + 1):
        total = sum(freq_cnt[i:i+m])
        if total >= max_tot:
            max_tot = total
            target = list(range(i,i+m))

    target = [i - n if i > n else i for i in target]

    ans, now, temp_score = 0, moles[0][0], []
    for time, idx, score in moles:
        if now != time:
            ans += max(temp_score) if len(temp_score) != 0 else 0
            now = time
            temp_score = []
        
        if idx in target:
            temp_score.append(score)
        
        
    return ans

print(solution(7, 2, [[7, 5, 6], [2, 1, 10], [6, 6, 6], [2, 2, 10], [3, 2, 10], [5, 5, 6], [8, 6, 6], [3, 1, 10]]))