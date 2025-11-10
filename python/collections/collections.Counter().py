from collections import Counter

number_shoes = int(input())
shoe_sizes = list(map(int, input().split()))

N = int(input())

total = Counter(shoe_sizes)
income = 0

for n in range(N):
    size, price = map(int, input().split())
    if size not in shoe_sizes:
        continue
    elif total[size] > 0:
        income += price
        total[size] -= 1

print(income)
        



