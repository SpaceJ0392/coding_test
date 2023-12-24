letter_list = ["A", "E", "I", "O", "U"]
word_list = {}
cnt = 0


def dfs(depth, word):
    global cnt
    if depth >= 5:
        return

    for letter in letter_list:
        word += letter
        if word_list.get(word) is None:
            cnt += 1
            word_list[word] = cnt
            dfs(depth + 1, word)

        word = word[:-1]


def solution(word):
    answer = 0
    dfs(0, "")

    return word_list.get(word)


print(solution("AAAAE"))  # 6
print(solution("I"))  # 1563
print(solution("EIO"))  # 1189
