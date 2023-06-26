# countConstruct
def countConstruct(phrase, list, memo = {}):
    if phrase in memo: return memo[phrase]
    if phrase == '': return 1

    count = 0

    for word in list:
        if len(phrase) >= len(word) and phrase[:len(word)] == word:
            count = count + countConstruct(phrase[len(word):], list, memo)
    
    memo[phrase] = count
    return count

# countConstruct
print(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'boar']))
print(countConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))


# canConstruct
def canConstruct(phrase, list, memo = {}):
    if phrase in memo: return memo[phrase]
    if phrase == '': return True

    for word in list:
        if len(phrase) >= len(word) and phrase[:len(word)] == word:
            if canConstruct(phrase[len(word):], list, memo): 
                memo[phrase] = True
                return True
    
    memo[phrase] = False
    return False


# canConstruct
print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'boar']))
print(canConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))


# allConstruct
def allConstruct(phrase, list, memo = {}):
    if phrase in memo: return memo[phrase]
    if phrase == '': return []

    ways = []

    for word in list:
        if len(phrase) >= len(word) and phrase[:len(word)] == word:
            if allConstruct(phrase[len(word):], list, memo): 
                ways.append(word)
    
    memo[phrase] = ways
    return ways

# countConstruct
print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(allConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'boar']))
print(allConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))