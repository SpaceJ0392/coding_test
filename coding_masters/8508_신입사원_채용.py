# union-find 고려
# 순서 고려

# n = int(input())
# parents = list(range(1,n + 1))

# target = []
# for i in range(n):
#     f_score, i_score = map(int, input().split())
#     target.append((i, f_score, i_score))


# def find_parent(child):
#     if parents[child] == child + 1:
#         return parents[child]
#     else:
#         return find_parent(parents[child] - 1)

# def union(child1, child2):
#     p1 = find_parent(child1)
#     p2 = find_parent(child2)
#     if p1 >= p2:
#         parents[p1 - 1] = p2
#     else:
#         parents[p2 - 1] = p1
        
# for i in range(n):
#     t_idx, tf_score, ti_score = target[i] # 현재 비교 대상
#     for idx, f_score, i_score in target:
#         if t_idx == idx: continue
#         if (tf_score >= f_score and ti_score < i_score) or (tf_score <= f_score and ti_score > i_score):
#             union(i, idx)


# for i in parents:
#     print(i, end=' ')

# # another way
# """
# 일단 받은 데이터를 정렬한다.
# 서류 점수 순, 면접 점수 순으로

# 서류 점수가 같고, 면접 점수도 같은 경우를 제외하고는, 정렬하였으므로, 면접 점수로 순위가 판가름이 난다.
# - 면접 점수가 target 보다 높으면, 같은 등수
# - 면접 점수가 target 보다 낮으면, 같은 등수 아님
# """

# n = int(input())
# ranking = [0] * n

# target = []
# for i in range(n):
#     f_score, i_score = map(int, input().split())
#     target.append((i, f_score, i_score))

# target.sort(reverse=True, key=lambda x : (x[0], x[1]))

# rank = 1
# for t_idx, tf_score, ti_score in target:
#     cnt = 0
#     for idx, f_score, i_score in target:
#         if t_idx == idx: # 자기 자신
#             ranking[t_idx] = rank
#         elif tf_score == f_score and ti_score == i_score: # 자기 자신과 동일한 값을 같는 타인
#             ranking[t_idx], ranking[idx] = rank, rank
#             cnt += 1
#         elif tf_score == f_score and ti_score > i_score: #
#             pass
#         elif tf_score == f_score and ti_score < i_score:
#             pass

n = int(input())
target = []
for i in range(n):
    f_score, i_score = map(int, input().split())
    target.append((f_score, i_score))
    
f_score_list = sorted(target, key=lambda x: x[0])
s_score_list = sorted(target, key=lambda x: x[1])

ranking, temp = []
rank = 1
while True:
    s_score = s_score_list.pop()
    if s_score not in temp:
        temp.append(s_score)
    else:
        
    if f_score_list and s_score_list: break
    