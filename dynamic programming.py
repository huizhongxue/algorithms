def howSum(n, list, memo = {}):
    memo[0] = []
    if n in memo: return memo[n]
    if n < 0: return None
    for x in list:
        if (howSum(n-x, list, memo) != None): 
            memo[n] = memo[n-x]
            memo[n].append(x)
            return memo[n]
    memo[n] = None
    return None


print(howSum(7, [2, 4], {}))
print(howSum(7, [5, 3, 4, 7], {}))