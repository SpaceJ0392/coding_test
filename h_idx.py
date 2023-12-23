def solution(citations):
    h_idx = 0
    for read in range(len(citations)):
        cnt = 0
        for cit in citations:
            if cit >= read:
                cnt += 1
            if cnt == read:
                h_idx = read
                break

    return h_idx


print(solution([3, 4]))


def othersolution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):  # [지금 몇 편이 남았는가? -> 모든 인용횟수가 이 값보다 큰가?(가장 작은 값이 이 값보다 큰가?)]
        if citations[i] >= l - i:
            return l - i
    return 0

"""
정리 
정렬을 통해 가장 작은 값 부터 배치하고, 전체 논문 수에서 논문의 개수를 빼 남은 논문의 개수에 대해 
가장 작은 위치에서의 인용 횟수보다 작으면, 어떻게 하든 h_idx를 만족하지 못하므로 거름.
"""


print(othersolution([3, 0, 6, 1, 5]))
