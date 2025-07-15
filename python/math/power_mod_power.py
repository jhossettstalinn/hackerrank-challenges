try:
    a = int(input())
    b = int(input())
    m = int(input())

    print(pow(a,b))
    print(pow(a, b, m))
except ValueError:
    print("Invalid input. Please enter integers only.")
