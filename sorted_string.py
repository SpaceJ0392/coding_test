def solution(strings, n):
    strings.sort(key=lambda x: x[n])

    idx_list = []
    for string in strings:
        idx_list.append(string[n])

    for i in range(len(idx_list) - 1):
        if idx_list[i] == idx_list[i + 1]:
            print(sorted(strings[i : i + 2]), type(strings[i : i + 2].sort))
            print(strings[i + 2 :], type(strings[i + 2 :]))

    return strings


print(solution(["abce", "abcd", "cdx"], 2))
