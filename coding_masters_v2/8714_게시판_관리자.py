n = int(input())
seq1 = input().split()
seq2 = input().split()

cnt = 0
for i in range(n):
    if seq1[i] != seq2[i]:
        cnt += 1

if cnt == 3 : print(3)
elif cnt == 4 : print(2)
else : print(0)