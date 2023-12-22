def solution(citations):
    h_idx = 0
    for read in range(len(citations)):
        cnt = 0
        for cit in citations:
            if cit >= read: cnt += 1
            if cnt == read:
                h_idx = read
                break

    return h_idx

print(solution([3, 4]))

# 분석 필요
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0