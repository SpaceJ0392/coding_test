def count_valid_permutations(n, sentence1, sentence2):
    # 두 문장을 단어 리스트로 변환
    words1 = sentence1.split()
    words2 = sentence2.split()

    # 두 문장에서 등장하는 단어가 동일한지 확인
    if sorted(words1) != sorted(words2):
        return 0
    
    # 두 문장에서 단어의 위치가 동일한지 확인
    positions = {}
    for word in words1:
        positions[word] = []

    for i in range(n):
        positions[words1[i]].append(i)

    # 각 단어의 위치가 동일한지 확인
    for i in range(n):
        word = words2[i]
        if i not in positions[word]:
            return 0

    # 올바른 자리를 맞추기 위한 순열의 수를 계산
    from math import factorial

    def cycle_length(lst):
        visited = [False] * len(lst)
        cycles = []
        for i in range(len(lst)):
            if not visited[i]:
                cycle = []
                x = i
                while not visited[x]:
                    visited[x] = True
                    cycle.append(x)
                    x = lst[x]
                cycles.append(cycle)
        return cycles

    indices = list(range(n))
    perm = [indices[words1.index(words2[i])] for i in range(n)]

    cycles = cycle_length(perm)
    result = 1
    for cycle in cycles:
        result *= factorial(len(cycle))

    return result

# 입력 처리
n = int(input().strip())
sentence1 = input().strip()
sentence2 = input().strip()

# 결과 출력
print(count_valid_permutations(n, sentence1, sentence2))

