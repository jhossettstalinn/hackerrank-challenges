def maximize_it(lists, M):
    """
    Given `lists` (a list of K lists of integers) and modulus M,
    returns the maximum possible value of (sum of squares) % M
    when picking one element from each list.
    """
    dp = {0}
    for lst in lists:
        # Precompute each element's square mod M
        squares_mod = [ (x*x) % M for x in lst ]
        new_dp = set()
        for r in dp:
            for s in squares_mod:
                new_dp.add((r + s) % M)
        dp = new_dp
    return max(dp)


if __name__ == '__main__':
    K, M = map(int, input().split())
    lists = []
  
    for _ in range(K):
        data = list(map(int, input().split()))
        Ni, elements = data[0], data[1:]
        lists.append(elements)

    result = maximize_it(lists, M)
    print(result)
