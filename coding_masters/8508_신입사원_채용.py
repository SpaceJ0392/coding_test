# union-find 고려
# 순서 고려

n = int(input())
parents = list(range(1,n + 1))

target = []
for i in range(n):
    f_score, i_score = map(int, input().split())
    target.append((i, f_score, i_score))


def find_parent(child):
    if parents[child] == child + 1:
        return parents[child]
    else:
        return find_parent(parents[child] - 1)

def union(child1, child2):
    p1 = find_parent(child1)
    p2 = find_parent(child2)
    if p1 > p2:
        parents[p1 - 1] = p2
    else:
        parents[p2 - 1] = p1
        
for i in range(n):
    _, tf_score, ti_score = target[i] # 현재 비교 대상
    for idx, f_score, i_score in target:
        if tf_score == f_score and ti_score == i_score: continue
        if (tf_score > f_score and ti_score < i_score) or (tf_score < f_score and ti_score > i_score):
            union(i, idx)


for i in parents:
    print(i, end=' ')