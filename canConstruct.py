# indicator function
def canConstruct(phrase, list, memo = {}):
    if phrase in memo: return memo[phrase]
    if phrase == '': return True

    I = 0

    for word in list:
        if len(phrase) >= len(word) and phrase[:len(word)] == word:
            I = I + canConstruct(phrase[len(word):], list)
    
    memo[phrase] = bool(I)
    return bool(I)

# no indicator function
def caanConstruct(phrase, list, memo = {}):
    if phrase in memo: return memo[phrase]
    if phrase == '': return True

    for word in list:
        if len(phrase) >= len(word) and phrase[:len(word)] == word:
            if canConstruct(phrase[len(word):], list): 
                memo[phrase] = True
                return True
    
    memo[phrase] = False
    return False



print(caanConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(caanConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'boar']))
print(caanConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(caanConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))