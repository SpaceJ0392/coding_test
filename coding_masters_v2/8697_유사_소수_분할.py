import math

n = int(input())


def get_prime(end):
    prime = [True] * (end + 1)

    for x in range(2, int(math.sqrt(end)) + 1):
        for t in range(x, end + 1, x):
            if x == t or prime[t] == False:
                continue
            prime[t] = False

    prime = [i for i in range(2, len(prime)) if prime[i] == True]
    pseudo_prime = [(prime[i] * prime[j]) for i in range(len(prime) - 1)
                    for j in range(i + 1, len(prime)) if prime[i] * prime[j] <= end]

    return sorted(pseudo_prime)


prime = get_prime(n)

flag = False
visited = []


def dfs(prime, visited, lev, tot):
    global flag
    if lev == 3:
        if tot < n and (n - tot) not in visited:
            flag = True
        return

    for num in prime:
        if num not in visited and tot + num < n:
            visited.append(num)
            dfs(prime, visited, lev + 1, tot + num)
            visited.pop()

            if flag:
                return


dfs(prime, visited, 0, 0)
print('possible') if flag else print('impossible')
