def min_lines_needed(N):
    # 초기 직선 개수와 만들어지는 영역의 개수를 설정
    lines = 0
    regions = 1
    
    # 더 많은 영역이 필요할 때까지 직선의 개수를 증가시키며 확인
    while regions < N:
        lines += 1
        regions = (lines * (lines + 1)) // 2 + 1
    
    return lines

# 입력 처리
N = int(input().strip())

# 결과 출력
print(min_lines_needed(N))
