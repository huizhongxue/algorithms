def canConstruct(phrase, list, memo = {}):
    if phrase in memo: return memo[phrase]
    if phrase == '': return True

    I = 0

    for word in list:
        if len(phrase) >= len(word) and phrase[:len(word)] == word:
            I = I + canConstruct(phrase[len(word):], list)
    
    memo[phrase] = bool(I)
    return bool(I)




print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'boar']))
print(canConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))