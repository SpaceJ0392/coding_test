n = int(input())
targets = list(map(int, input().split()))

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

ans = targets[0]
for target in targets[1:]:
    ans = gcd(ans, target)

print(ans)