def solution(keymap, targets):
    answer = []
    key_dict = {}

    for key_string in keymap:
        for idx, key in enumerate(key_string):
            if not key_dict[key]:
                key_dict[key] = idx

    print(key_dict)
    return answer


solution(["ABACD", "BCEFD"], ["ABCD", "AABB"])
