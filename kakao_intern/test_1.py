def solution(friends, gifts):
    getting_list = [0] * len(friends)

    friends_idx = {}
    for idx, friend in enumerate(friends):
        friends_idx[friend] = idx

    gifts_list = [[0] * len(friends) for _ in range(len(friends))]  # 선물 1:1 매핑
    indices_list = [0] * len(friends)  # 선물 지수

    for gift in gifts:
        giver, receiver = gift.split()
        gifts_list[friends_idx[giver]][friends_idx[receiver]] += 1
        indices_list[friends_idx[giver]] += 1
        indices_list[friends_idx[receiver]] -= 1

    for giv_idx in range(len(gifts_list)):
        for rec_idx in range(giv_idx, len(gifts_list[0])):
            if giv_idx == rec_idx:
                continue

            if gifts_list[giv_idx][rec_idx] > gifts_list[rec_idx][giv_idx]:
                getting_list[giv_idx] += 1
            elif gifts_list[giv_idx][rec_idx] < gifts_list[rec_idx][giv_idx]:
                getting_list[rec_idx] += 1
            else:
                if indices_list[giv_idx] > indices_list[rec_idx]:
                    getting_list[giv_idx] += 1
                elif indices_list[giv_idx] < indices_list[rec_idx]:
                    getting_list[rec_idx] += 1

    return max(getting_list)


print(solution(
    ["joy", "brad", "alessandro", "conan", "david"],
    [
        "alessandro brad",
        "alessandro joy",
        "alessandro conan",
        "david alessandro",
        "alessandro david",
    ],
))
