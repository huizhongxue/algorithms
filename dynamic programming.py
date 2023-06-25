def canSum(n, list, memo = {}):
    if n in memo: return memo[n]
    if n == 0: return True
    if n < 0: return False
    for x in list:
        if (canSum(n-x, list, memo) == True): 
            memo[n] = True
            return True
    memo[n] = False
    return False


print(canSum(7, [2, 4], {}))
print(canSum(7, [5, 3, 4, 7], {}))