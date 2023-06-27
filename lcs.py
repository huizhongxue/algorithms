def lcs(a, b, memo = {}):
    if (a, b) in memo: return memo[(a, b)]
    if a == '' or b == '': return 0

    m = 0

    if a[0] == b[0]: 
        m = 1 + lcs(a[1:], b[1:], memo)
    else:
        if lcs(a[1:], b, memo) > lcs(a, b[1:], memo):
            m = lcs(a[1:], b, memo)
        else:
            m = lcs(a, b[1:], memo)

    memo[(a, b)] = m
    return m

print(lcs("abcde", "ace", {}))
print(lcs("abc", "abc", {}))
print(lcs("abc", "def", {}))