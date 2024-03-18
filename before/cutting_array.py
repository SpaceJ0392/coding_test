def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)

    return answer


# 덱스에 1이 한개 라도 들어 가면 2,
# 인덱스에 2가 하나 라도 들어간 곳은 3

# 근데 열이 1인 행렬로 생각해 본다면
# 0 (0,0) 1 (0,1) 2 (0,2) 3 (1,0) 4 (1,1) 5 (1,2) 6 (2,0) 7 (2,1) 8 (2,2)
# 이런 식으로 볼수 있다.
# 이는 앞의 index 8번을 본다면, 8 (8//3, 8% 3)( 몫, 나머지)로 확인할 수 있다. 그리고 몫과 나머지 중 가장 큰값에 따라서 숫자가 들어 간다.


print(solution(3, 2, 5))
