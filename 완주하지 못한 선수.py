import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    a = 1
    return list(answer.keys())[0]

solution(["leo", "kiki", "eden"], ["eden", "kiki"])