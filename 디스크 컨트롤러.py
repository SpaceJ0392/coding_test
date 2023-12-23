import heapq


def solution(jobs):
    tot_sum, l = 0, len(jobs)  # 전체 작업 소요, 작업 크기
    now = 0  # 현재 작업 시간
    delayed = []

    # 최초의 작업 지정
    jobs.sort(reverse=True)
    start, duration = jobs.pop()
    heapq.heappush(delayed, (duration, start))

    while jobs or delayed:
        # now 위치보다 작은 모든 시작시간의 작업을 대기열에 넣기
        # 생각해야 할 조건 - heap에 뭐가 있으면, 다 비우고 pop
        duration, start = heapq.heappop(delayed)

        # 작업 시간 조정
        now = max(now + duration, start + duration)
        tot_sum += now - start

        while jobs and jobs[-1][0] <= now:
            start, duration = jobs.pop()
            heapq.heappush(delayed, (duration, start))

        if jobs and len(delayed) == 0:
            start, duration = jobs.pop()
            heapq.heappush(delayed, (duration, start))

    return tot_sum // l


print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[7, 8], [3, 5], [9, 6]]))
print(solution([[1, 3], [7, 5], [9, 6]]))
