def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    print(phoneBook[1:])
    print(list(zip(phoneBook, phoneBook[1:])))
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

print(solution(["123","456","789"]))