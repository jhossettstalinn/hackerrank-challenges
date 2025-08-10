M = int(input())
set_M = set(map(int, input().split()))

N = int(input())
set_N = set(map(int, input().split()))

diff = set()
diff.update(set_M.difference(set_N))
diff.update(set_N.difference(set_M))

for i in sorted(diff):
    print(i)
