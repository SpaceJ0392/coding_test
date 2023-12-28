def solution(name):
    answer = 0
    now = 0
    front, rear = 1, len(name) - 1

    # A ~ N 접근 최소 거리
    letter_dict = {
        chr(letter): idx for idx, letter in enumerate(range(ord("A"), ord("N") + 1))
    }

    # O ~ Z 접근 최소 거리
    letter_dict.update(
        {
            chr(letter): idx
            for idx, letter in enumerate(range(ord("Z"), ord("N"), -1), 1)
        }
    )

    while front <= rear:
        if name[now] != "A":
            answer += letter_dict[name[now]]

        # A가 아닌게 나올 때 까지 좌우로 이동시키며 탐색
        while name[front] == "A" and name[rear] == "A":
            front += 1
            rear -= 1

        # front와 rear 중 선택 - 더 빨리 나온 쪽을 선택해야함...
        if name[front] != "A":
            now = front
        else:
            now = rear

        answer += front

    return answer


print(solution("AAABAAABA"))
