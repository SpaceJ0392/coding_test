def solution(survey, choices):
    answer = ""
    character_type_list = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0,
    }
    for ch_type, choice in zip(survey, choices):
        if choice == 4:
            continue

        ne, po = ch_type[0], ch_type[1]
        if choice // 4 > 0:
            character_type_list[po] += choice % 4
        else:
            character_type_list[ne] += 4 - choice % 4

    target = list((character_type_list.items()))
    print(target)
    for idx in range(0, len(character_type_list), 2):
        if target[idx][1] > target[idx + 1][1]:
            answer += target[idx][0]
        elif target[idx][1] < target[idx + 1][1]:
            answer += target[idx][0]
        else:
            answer += min(target[idx][0], target[idx + 1][0])

    return answer


solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])
