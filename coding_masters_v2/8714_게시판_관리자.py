n = int(input())
seq1 = input().split()
seq2 = input().split()

target_seq = []
for i in range(n - 1):
    for j in range(i + 1, n):
        temp = seq1.copy()
        temp[i], temp[j] = temp[j], temp[i]
        target_seq.append(temp)

seq_cnt = 0
for target in target_seq:
    cnt = 0
    for i in range(n):
        if target[i] != seq2[i]: cnt += 1
    
    if cnt == 2: seq_cnt += 1

print(seq_cnt)