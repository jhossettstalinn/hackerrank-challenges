import sys

data = {'a':'', 'b':'', 'c':'', 'd':''}
for i in data:
    data[i] = int(sys.stdin.readline().strip())

Calc = data['a']**data['b'] + data['c']**data['d']
print(Calc)
