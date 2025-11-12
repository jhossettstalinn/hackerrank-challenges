from collections import defaultdict

n, m = map(int, input().split())

words_n = [input().strip() for i in range(n)]
words_m = [input().strip() for j in range(m)]

position = defaultdict(list)
for i, word in enumerate(words_n, 1): 
    position[word].append(i)

for j in words_m:
    if j in position:
        print(" ".join(map(str, position[j])))
    else:
        print(-1)


