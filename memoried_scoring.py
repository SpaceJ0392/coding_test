def solution(name, yearning, photo):
    answer = []
    score_dict = {}

    for idx in range(len(name)):
        score_dict[name[idx]] = yearning[idx]

    print(type(score_dict['may']))
    #     for members in photo:
    #         score = 0

    #         for name in members:
    #             score += score_dict.get(name)

    #         answer.append(score)
    return answer
