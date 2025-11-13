
number_test_cases = int(input())
list = []

for n in range(number_test_cases):
    a, b = input().split()
    list.append((a, b))

for a, b in list:
    try:
        result = int(a) // int(b)
        print(result)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)