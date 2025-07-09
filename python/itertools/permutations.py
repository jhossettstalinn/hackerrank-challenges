from itertools import permutations

S, k = input().split()
S = S.upper()
k = int(k)

perms = list(permutations(sorted(S), k))

for perm in perms:
    print(''.join(perm))
