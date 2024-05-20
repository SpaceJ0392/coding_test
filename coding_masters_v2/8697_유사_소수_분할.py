import math

n = int(input())

if n > 2:
    # 유사 소수 구하기
    def get_prime(end):
        prime = [True] * (end + 1)

        for x in range(2, int(math.sqrt(end)) + 1):
            for t in range(x, end + 1, x): 
                if x == t or prime[t] == False: continue
                prime[t] = False
        
        prime[2] = True
        prime = [i for i in range(2, len(prime)) if prime[i] == True]
        pseudo_prime = [(prime[i] * prime[j]) for i in range(1, len(prime) - 1) for j in range(i + 1, len(prime)) if prime[i] * prime[j] <= end]

        return sorted(prime + pseudo_prime)

    prime = get_prime(n)

    flag = False
    visited = [1]
    def dfs(prime, visited, lev, tot):
        global flag
        if lev == 3:
            if tot < n and (n - tot) not in visited: flag = True
            return

        for num in prime:
            if num not in visited and tot + num < n:
                visited.append(num)
                dfs(prime, visited, lev + 1, tot + num)
                visited.pop()

                if flag: return

    dfs(prime, visited, 0, 0)
else:
    flag = False

print('possible') if flag else print('impossible')
