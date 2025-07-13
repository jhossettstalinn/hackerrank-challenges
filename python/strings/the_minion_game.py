def minion_game(s):
    kevin = stuart = 0
    vowels = 'AEIOU'
  
    for i, ch in enumerate(s):
        if ch in vowels:
            kevin += len(s) - i
        else:
            stuart += len(s) - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")         

if __name__ == '__main__':
    s = input()
    minion_game(s)
