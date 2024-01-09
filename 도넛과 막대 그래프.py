def solution(edges):
    res = [0] * 4
    out_graph = dict()
    in_graph = dict()

    for start, end in edges:
        if out_graph.get(start) is None:
            out_graph[start] = []

        if in_graph.get(end) is None:
            in_graph[end] = []

        out_graph[start].append(end)
        in_graph[end].append(start)

    # 생성 정점 : 나가기만 하는 점 중 그 길이가 1이 아닌 점
    created_node = [
        node
        for node in out_graph.keys()
        if in_graph.get(node) is None and len(out_graph[node]) > 1
    ]
    res[0] = created_node[0]

    # 1자 패턴 정점 : 나가는 점 X
    one_line_node = [node for node in in_graph.keys() if out_graph.get(node) is None]
    res[2] = len(one_line_node)

    # 8자 패전 정점 : 2번 나가는 점
    eight_node = [
        node
        for node in out_graph.keys()
        if len(out_graph[node]) == 2 and node != created_node[0]
    ]
    res[3] = len(eight_node)

    # 순환은 전체 그래프 수 중 1자와 8자를 제외한 나머지
    res[1] = len(out_graph[created_node[0]]) - (res[2] + res[3])

    # for node in out_graph[created_node[0]]:
    #     node_path = []
    #     while True:
    #         # 1자 패턴 : 나가는 점 X
    #         if out_graph.get(node) is None:
    #             res[2] += 1
    #             break
    #
    #         # 8자 패턴
    #         if len(out_graph[node]) >= 2:
    #             res[3] += 1
    #             break
    #
    #         # 순환 패턴
    #         if node in node_path:
    #             res[1] += 1
    #             break
    #
    #         # 패턴 해당 됨이 확인 될 때까지 이동
    #         node_path.append(node)
    #         node = out_graph[node][0]

    return res


print(
    solution(
        [
            [4, 11],
            [1, 12],
            [8, 3],
            [12, 7],
            [4, 2],
            [7, 11],
            [4, 8],
            [9, 6],
            [10, 11],
            [6, 10],
            [3, 5],
            [11, 1],
            [5, 3],
            [11, 9],
            [3, 8],
        ]
    )
)

print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))


# # 회전 패전 정점 : 생성 정점 포함 들어오는 점이 2개, 나가는 점이 1개.
# rotate_node = [node for node in in_graph.keys() if out_graph.get(node) is None]
# res[1] = len(rotate_node)
#
# # 1자 패턴 정점 : 나가는 점 X
# one_line_node = [node for node in in_graph.keys() if out_graph.get(node) is None]
# res[2] = len(one_line_node)
#
# # 8자 패전 정점 : 2번 나가는 점
# eight_node = [
#     node
#     for node in out_graph.keys()
#     if len(out_graph[node]) == 2 and node != created_node[0]
# ]
# res[3] = len(eight_node)
