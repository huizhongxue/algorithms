import math
import numpy as np

# Longest common subsequence
def longest_common_subsequence(a, b):
    common = {}
    if len(a) < len(b): 
        short = a
        long = b
    else: 
        short = b
        long = a
    for i in range(0, len(short), 1):
        common[i+1] = []
        for j in range(0, len(long), 1):
            if short[i] == long[j]:
                common[1].append((i, j))
    if len(short) == 1:
        if common[1]: return 1
        else: return 0
    for i in range(2, len(short)+1, 1):
        for x, y in common[i-1]:
            if x + 1 < len(short) and y + 1 < len(long):
                if short[x+i-1] == long[y+i-1]:
                    common[i].append((x, y))
    for i in range(len(short), 0, -1):
        if common[i]: return i
    return 0

x = 'hhhhhhababhhhhhhhhhhhhh'
y = 'iiiiiabai'

print(longest_common_subsequence(x, y))