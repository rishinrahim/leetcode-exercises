# Caesar Cipher Encrpytion
# You are given a list of string, group them if they are same after using Ceaser Cipher Encrpytion.
# Definition of "same", "abc" can right shift 1, get "bcd", here you can shift as many time as you want, the string will be considered as same.

# Example:

# Input: ["abc", "bcd", "acd", "dfg"]
# Output: [["abc", "bcd"], ["acd", "dfg"]]


from collections import defaultdict

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def group_ceasar(los):
    storage = defaultdict(list)

    for s in los:
        pos = [alphabet.index(c) for c in s]
        print(pos)
        minPos = min(pos)
        pos = [num - minPos for num in pos]
        print(tuple(pos))
        storage[tuple(pos)].append(s)
        print("---")

    return storage.values()

v=["abc", "bcd", "acd", "dfg", "ace", "bdf", "random"]
print(group_ceasar(v))
