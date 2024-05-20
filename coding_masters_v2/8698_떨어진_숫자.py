drop_n = list(input())
contain_n = list(input())

print('YES') if sorted(drop_n) == sorted(contain_n) else print('NO')