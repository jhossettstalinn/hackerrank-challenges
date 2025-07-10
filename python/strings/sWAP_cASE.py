def swap_case(s):
    #s = s.swapcase()
    s = ''.join([char.lower() if char.isupper() else char.upper() for char in s])
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
