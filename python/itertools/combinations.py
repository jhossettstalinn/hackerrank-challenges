
from itertools import combinations

def possible_combinations(String, k_value):

    String = sorted(String)

    if k_value <= len(String) and k_value > 0:
        for i in range(1, k_value + 1):
            for j in combinations(String, i):
                yield j
    else:
        print("k value must be a natural number less than or equal to the length of the string.")


if __name__ == '__main__':
    S, k = input().upper().split()
    k = int(k)
    for i in possible_combinations(S, k):
        print(''.join(i))
