def dvs(a, b):
    d_mod = divmod(a, b)
    n_div, n_mod = d_mod
    print(n_div)
    print(n_mod)
    print(d_mod)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    dvs(a, b)
